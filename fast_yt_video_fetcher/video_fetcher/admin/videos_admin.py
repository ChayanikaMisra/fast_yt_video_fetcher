from django.contrib import admin

from video_fetcher.models import YoutubeVideos


class YoutubeVideoFetcherAdmin(admin.ModelAdmin):
    list_display = ('youtube_video_id', 'title', 'description')
    search_fields = ('title', 'description')


admin.site.register(YoutubeVideos, YoutubeVideoFetcherAdmin)
