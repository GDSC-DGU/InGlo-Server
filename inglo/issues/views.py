from rest_framework import generics, status, views
from rest_framework.response import Response
from .serializers import IssueSerializer, IssueListSerializer, IssueCommentSerializer
from .services.issue_services import IssueService
from .services.comment_service import CommentService
from rest_framework.permissions import IsAuthenticated

class RecommendedIssueListView(generics.ListAPIView):

    serializer_class = IssueListSerializer

    def get_queryset(self):
        """
        좋아요 수와 조회수를 기반으로 랭킹을 매긴 후,
        가장 높은 랭킹의 이슈 3개를 반환.
        좋아요 하나 = 조회수 10개로 계산하여 랭킹 매김.
        단, 생성된지 72시간 이내의 글에 대해서만.
        """

        return IssueService.get_recommended_issues()


class SDGsIssueListView(generics.ListAPIView):
    
    serializer_class = IssueListSerializer

    def get_queryset(self):
        """
        클라이언트로부터 받은 SDGs 값을 기반으로
        해당 SDGs 카테고리와 관련된 최신 10개의 이슈를 반환.
        """

        sdgs_number = self.kwargs.get('sdgs')
        return IssueService.get_issues_by_sdgs(sdgs_number)

class IssueDetailView(views.APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        조회수를 1 증가시킨 후 해당 이슈 반환
        """

        issue_id = self.kwargs.get('issue_id')
        issue = IssueService.get_issue_with_increased_view(issue_id)
        if issue:
            serializer = IssueSerializer(issue,context={'request': request})
            return Response(serializer.data)
        else:
            return Response({"error": "Issue not found"}, status=404)

class IssueCreateView(views.APIView):
        
    def post(self, request, *args, **kwargs):
        """
        외부 News API로부터 데이터를 가져와
        분류모델을 돌려서
        Issue, IssueList에 저장
        """

        keyword = 'SDGs'  
        IssueService.update_issues_from_news(keyword)
        return Response({"message": "Issues successfully updated."}, status=status.HTTP_200_OK)

class IssueLikeView(views.APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        좋아요 추가 또는 삭제
        """

        issue_id = self.kwargs.get('issue_id')
        liked = IssueService.toggle_like(request.user, issue_id)
        if liked:
            return Response({"message": "Like added successfully."}, status=201)
        else:
            return Response({"message": "Like removed successfully."}, status=204)
    
class IssueCommentCreate(views.APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        댓글 생성
        """

        issue_id = self.kwargs.get('issue_id')
        comment = CommentService.create_comment(user=request.user, issue_id=issue_id, data=request.data)
        serializer = IssueCommentSerializer(comment)
        return Response(serializer.data, status=201)

class IssueCommentUpdate(views.APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        """
        댓글 수정
        """

        comment_id = self.kwargs.get('comment_id')
        comment = CommentService.update_comment(user=request.user, comment_id=comment_id, data=request.data)
        serializer = IssueCommentSerializer(comment)
        return Response(serializer.data)

class IssueCommentDelete(views.APIView):

    permission_classes = [IsAuthenticated]
    
    def delete(self, request, *args, **kwargs):
        """
        댓글 삭제
        """
        
        comment_id = self.kwargs.get('comment_id')
        CommentService.delete_comment(user=request.user, comment_id=comment_id)
        return Response({"message": "Comment deleted successfully."}, status=204)