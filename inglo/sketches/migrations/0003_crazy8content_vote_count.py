# Generated by Django 4.2.6 on 2024-02-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sketches', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crazy8content',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]
