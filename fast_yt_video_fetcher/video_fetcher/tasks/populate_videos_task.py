import json
import logging

from video_fetcher.models import YoutubeVideos
from service_config.celery import app
from services import youtube_service

logger = logging.getLogger(__name__)


@app.task
def populate_videos_from_yt_task():
    """
        Celery task to all youtube API asynchronously every 10 secs
        to populate yt_videos table
    """
    youtube_response = json.loads(
        youtube_service.search_video_data("video", "date", "2021-02-16T00:00:00Z", "cricket", "snippet"))
    logger.info("youtube api called")
    YoutubeVideos.save_videos_from_youtube_response(youtube_response)
