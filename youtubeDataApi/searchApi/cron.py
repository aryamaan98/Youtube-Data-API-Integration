import requests
import json
from . utils import _extract_videos_necessary_details, _save_video_detils_in_db
from . import config


def get_recent_youtube_videos_details():
    youtube_api_response = requests.get(
        config.YOUTUBE_SEARCH_URL, params=config.params)
    print('Youtube API Response: ', youtube_api_response.text)
    youtube_api_response = json.loads(youtube_api_response.text)
    videos_details = _extract_videos_necessary_details(
        youtube_api_response.get('items', []))
    if videos_details:
        _response = _save_video_detils_in_db(videos_details)
    return videos_details
