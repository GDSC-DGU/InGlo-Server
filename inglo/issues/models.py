from django.db import models
from users.models import User

class Issue(models.Model):
    link = models.URLField()
    writer = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class IssueList(models.Model):
    issue = models.OneToOneField(Issue, on_delete=models.CASCADE, related_name='list')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    country = models.IntegerField() # 국가 번호로
    sdgs = models.IntegerField() # SDGs 번호로
    created_at = models.DateTimeField(auto_now_add=True)

class IssueComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

class IssueLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)