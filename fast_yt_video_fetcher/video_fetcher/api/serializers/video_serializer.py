from rest_framework import serializers

from video_fetcher.models import YoutubeVideos


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideos
        fields = ['youtube_video_id', 'title', 'description', 'publishing_datetime']