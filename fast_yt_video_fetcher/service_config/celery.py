from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service_config.settings")
app = Celery("fast_yt_video_fetcher")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_default_queue = "fast_yt_video_fetcher_celery"

app.autodiscover_tasks()
