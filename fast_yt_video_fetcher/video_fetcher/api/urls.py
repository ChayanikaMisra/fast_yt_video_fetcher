from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
from video_fetcher.api.views.videos_viewset import VideoDetailsViewSet

router = DefaultRouter()
router.register(r"videos", VideoDetailsViewSet, basename='video_details')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
