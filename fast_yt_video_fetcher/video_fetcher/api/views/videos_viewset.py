from rest_framework import viewsets, pagination, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from video_fetcher.api.serializers.video_serializer import VideoSerializer
from video_fetcher.models import YoutubeVideos


class VideoDetailsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = VideoSerializer

    def get_queryset(self):
        page_size = self.request.query_params.get("page_size")
        pagination.PageNumberPagination.page_size = page_size
        queryset = YoutubeVideos.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = VideoSerializer(queryset, many=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = VideoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def search(self, request):
        queryset = YoutubeVideos.objects.all()
        title_search = self.request.query_params.get("title")
        description_search = self.request.query_params.get("description")
        if title_search:
            queryset = YoutubeVideos.objects.filter(title__contains=title_search)
        if description_search:
            queryset = YoutubeVideos.objects.filter(description__contains=description_search)
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)
