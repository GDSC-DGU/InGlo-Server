# Generated by Django 4.2.6 on 2024-02-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
