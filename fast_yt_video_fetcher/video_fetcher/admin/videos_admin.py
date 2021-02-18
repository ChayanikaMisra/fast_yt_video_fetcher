from django.contrib import admin

from video_fetcher.models import YoutubeVideos


class YoutubeVideoFetcherAdmin(admin.ModelAdmin):
    list_display = ('youtube_video_id', 'title', 'description','publishing_datetime')
    search_fields = ('title', 'description')
    ordering = ('-publishing_datetime',)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(YoutubeVideos, YoutubeVideoFetcherAdmin)
