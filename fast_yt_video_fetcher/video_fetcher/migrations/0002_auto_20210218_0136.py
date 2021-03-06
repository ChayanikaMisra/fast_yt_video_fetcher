# Generated by Django 3.1.6 on 2021-02-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_fetcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='youtubevideos',
            options={'ordering': ['-publishing_datetime']},
        ),
        migrations.AddIndex(
            model_name='youtubevideos',
            index=models.Index(fields=['title'], name='yt_videos_title_42e0b0_idx'),
        ),
        migrations.AddIndex(
            model_name='youtubevideos',
            index=models.Index(fields=['description'], name='yt_videos_descrip_948ba5_idx'),
        ),
    ]
