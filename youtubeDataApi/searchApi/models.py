import uuid
from django.db import models
from django.utils import timezone


class VideosDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    youtube_video_id = models.TextField(max_length=15, null=False, unique=True)
    title = models.TextField(null=False)
    description = models.TextField(null=True)
    publish_datetime = models.DateTimeField(null=False)
    thumbnail_url = models.URLField(max_length=255, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)


class ApiKeys(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    api_key = models.TextField(max_length=255, null=False, unique=True)
    last_used = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
