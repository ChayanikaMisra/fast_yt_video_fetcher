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
        indexes = [
            models.Index(fields=['title', ]),
            models.Index(fields=['description', ]),
        ]

    @staticmethod
    def create_videos(yt_video_id, title, description, publishing_datetime, thumbnails, channel_title):
        """
            If video is not present in db create the video otherwise get the video
        """
        video, created = YoutubeVideos.objects.get_or_create(youtube_video_id=yt_video_id,
                                                             title=title,
                                                             description=description,
                                                             publishing_datetime=publishing_datetime,
                                                             thumbnails=thumbnails,
                                                             channel_title=channel_title
                                                             )
        if created:
            video.save()


    @staticmethod
    def save_videos_from_youtube_response(yt_response):
        for item in yt_response["items"]:
            yt_video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            thumbnails = item["snippet"]["thumbnails"]
            publishing_datetime = item["snippet"]["publishTime"]
            channel_title = item["snippet"]["channelTitle"]
            YoutubeVideos.create_videos(yt_video_id, title, description, publishing_datetime, thumbnails, channel_title)
