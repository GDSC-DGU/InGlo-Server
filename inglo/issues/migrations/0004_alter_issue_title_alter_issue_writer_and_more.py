# Generated by Django 4.2.6 on 2024-02-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_alter_issue_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='issue',
            name='writer',
            field=models.CharField(blank=True, default='unknown', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='issuelist',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
