from django.conf import settings


YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

NUMBER_OF_RESPONSES = 10
SEARCH_KEYWORD = 'India vs England Cricket'
PUBLISHED_AFTER = '2021-03-16T00:00:00+00:00'

params = {
    'part': 'snippet',
    'q': SEARCH_KEYWORD,
    'maxResults': NUMBER_OF_RESPONSES,
    'type': 'video',
    'publishedAfter': PUBLISHED_AFTER,
    'order': 'date',
    'key': settings.YOUTUBE_SEARCH_API_KEY,
}