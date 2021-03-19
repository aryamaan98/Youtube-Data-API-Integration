import requests
import json
from dateutil.parser import parse
from django.db.models import Q
from .models import VideosDetail
from . import config


def _extract_videos_necessary_details(responses):
    videos_details = []
    if not responses:
        print('No videos found')
        return videos_details

    for response in responses:
        video_details = {
            'youtube_video_id': response.get('id', {}).get('videoId', None),
            'title': response.get('snippet', {}).get('title', None),
            'description': response.get('snippet', {}).get('description'),
            'publish_datetime': response.get('snippet', {}).get('publishTime', None),
            'thumbnail_url': response.get('snippet', {}).get('thumbnails', {}).get('default', {}).get('url', '')
        }
        if not video_details['publish_datetime'] or not video_details['title'] or not video_details['youtube_video_id']:
            continue
        video_details['publish_datetime'] = parse(
            video_details['publish_datetime'])
        videos_details.append(video_details)

    print('Videos Details', videos_details)
    return videos_details


def _save_video_detils_in_db(videos_details):
    video_model_objects = [
        VideosDetail(
            youtube_video_id=video_details['youtube_video_id'],
            title=video_details['title'],
            description=video_details['description'],
            publish_datetime=video_details['publish_datetime'],
            thumbnail_url=video_details['thumbnail_url']
        )
        for video_details in videos_details
    ]
    response = VideosDetail.objects.bulk_create(
        objs=video_model_objects, ignore_conflicts=True)
    print('Response', response)
    print('Successfull saved in database !')
    return response


def get_videos_details_for_keyword(search_keyword):
    videos_details = VideosDetail.objects.filter(Q(title__icontains=search_keyword) | Q(
        description__icontains=search_keyword)).order_by('publish_datetime').reverse()
    print('Vidoes Details', videos_details)
    all_video_details = [
        {
            'youtube_video_id': detail.youtube_video_id,
            'title': detail.title,
            'description': detail.description,
            'publish_datetime': detail.publish_datetime,
            'thumbnail_url': detail.thumbnail_url
        }
        for detail in videos_details
    ]
    return all_video_details


def get_all_videos_details():
    all_details = VideosDetail.objects.all().order_by('publish_datetime').reverse()
    all_video_details = [
        {
            'youtube_video_id': detail.youtube_video_id,
            'title': detail.title,
            'description': detail.description,
            'publish_datetime': detail.publish_datetime,
            'thumbnail_url': detail.thumbnail_url
        }
        for detail in all_details
    ]
    return all_video_details
