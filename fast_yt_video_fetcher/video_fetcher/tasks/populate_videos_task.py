import json
import logging
from datetime import datetime, timedelta

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
    published_after = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    youtube_response = json.loads(
        youtube_service.search_video_data("video", "date", published_after, "cricket", "snippet"))
    logger.info("youtube api called")
    YoutubeVideos.save_videos_from_youtube_response(youtube_response)
