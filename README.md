# fast youtube video fetcher

- Calls youtube API using **publish_after=(current_day minus 2 day)** in the background using [CELERY_BEAT_SCHEDULE](https://github.com/ChayanikaMisra/fast_yt_video_fetcher/blob/master/fast_yt_video_fetcher/service_config/settings.py#L135)
- Creates and stores youtube API response videos in database [youtube_video](https://github.com/ChayanikaMisra/fast_yt_video_fetcher/blob/update-readme/fast_yt_video_fetcher/video_fetcher/models/youtube_videos.py#L40)
- Exposes a GET API for users to fetch latest videos [fetch_videos_api](https://github.com/ChayanikaMisra/fast_yt_video_fetcher/blob/master/fast_yt_video_fetcher/video_fetcher/api/views/videos_viewset.py#L19)
- Exposes a search API for users to search using title and description [search_api](https://github.com/ChayanikaMisra/fast_yt_video_fetcher/blob/master/fast_yt_video_fetcher/video_fetcher/api/views/videos_viewset.py#L29)
- Find the APIs cURL [here](https://github.com/ChayanikaMisra/fast_yt_video_fetcher#api-doc)
- Dashboard: [here](http://127.0.0.1:8000/admin/)

## Local Setup
- Go into the fast_yt_video_fetcher/fast_yt_video_fetcher/
```
cd fast_yt_video_fetcher/fast_yt_video_fetcher/
```
- Create django admin superuser
```
python manage.py createsuperuser <username>
```
- Run docker-compose up to run the app
```
docker-compose up --build
```
- Find the app running in http://127.0.0.1:8000/admin/
- Login to the dashboard using the superuser credentials to view the videos


**In case ```docker-compose up``` does not populate the db**
Run these commands:
```
python manage.py runserver
```
```
celery -A service_config worker -B -l info
```

## Celery task to call youtube API
- Async task which calls youtube API [celery task](https://github.com/ChayanikaMisra/fast_yt_video_fetcher/blob/master/fast_yt_video_fetcher/video_fetcher/tasks/populate_videos_task.py)
- This task is called at an interval of 10s using celery beat scheduler [CELERY_BEAT_SCHEDULE](https://github.com/ChayanikaMisra/fast_yt_video_fetcher/blob/master/fast_yt_video_fetcher/service_config/settings.py#L135)

## API Doc:
- http://{base url}/api/v1/videos/?page_size=1
    ```Query Params:
        page_size : specifies the number of objects per page_size

       Response:
                {
                    "count": 5,
                    "next": "http://127.0.0.1:8000/api/v1/videos/?page=2&page_size=1",
                    "previous": null,
                    "results": [
                        {
                            "youtube_video_id": "pEzybK8wzFw",
                            "title": "Best Moments In Cricket History | Top Cricket Moments | MB2T",
                            "description": "Best Moments In Cricket History | Top Cricket Moments | MB2T.",
                            "publishing_datetime": "2021-02-17T17:00:18Z"
                        }
                    ]
                }

    ```

- http://{base url}/api/v1/videos/search/?title={search title}&description={search description}>
    ```Query Params:
        title : search video objects having title param
        description: search video objects having description param

       Response:
                [
                    {
                        "youtube_video_id": "aVox3_bKr5Y",
                        "title": "CM KCR Cricket Trophy Final at Siddipet Cricket Stadium | T News Live",
                        "description": "TNews is a 24/7 Telugu news channel now on YouTube.The first Telangana news channel featuring best news from all around the world. We deliver breaking ...",
                        "publishing_datetime": "2021-02-17T16:42:13Z"
                    }
                ]

    ```

