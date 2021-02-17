from django.contrib.postgres.fields import JSONField
from django.db import models

from video_fetcher.models import AutoTimestampedModel


class YoutubeVideos(AutoTimestampedModel):
    youtube_video_id = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    publishing_datetime = models.DateTimeField(null=True, blank=True)
    thumbnails = JSONField(null=True, blank=True)
    channel_title = models.URLField(max_length=200)

    class Meta:
        db_table = "yt_videos"
        ordering = ['-publishing_datetime']

    @staticmethod
    def create_videos(yt_video_id, title, description, publishing_datetime, thumbnails, channel_title):
        video, created = YoutubeVideos.objects.get_or_create(youtube_video_id=yt_video_id,
                                                             title=title,
                                                             description=description,
                                                             publishing_datetime=publishing_datetime,
                                                             thumbnails=thumbnails,
                                                             channel_title=channel_title
                                                             )
        if created:
            video.save()
