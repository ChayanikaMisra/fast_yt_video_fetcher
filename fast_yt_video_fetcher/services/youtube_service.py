import requests


class YoutubeService:
    base_url = "https://www.googleapis.com/youtube/v3/"
    api_key = "AIzaSyCHHU9cXfMSwGsoE_SXZ9f0fXW_mFDI7Qc"

    def search_video_data(self, content_type, order_by, published_after, search_param, part):
        payload = {}
        headers = {}
        endpoint = "search?key={}&type={}&order={}&publishedAfter={}&q={}&part={}&maxResults=5".format(
            self.api_key,
            content_type,
            order_by,
            published_after,
            search_param,
            part
        )
        url = self.base_url + endpoint
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text
