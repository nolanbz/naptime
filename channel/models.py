from django.conf import settings
from django.db import models
from django.utils import timezone


class Channel(models.Model):
    creator          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    channel_name     = models.CharField(max_length=200)
    channel_url      = models.CharField(max_length=200)
    video_count      = models.CharField(max_length=200)
    channel_location = models.CharField(max_length=200)
    subscriber_count = models.CharField(max_length=200)
    email            = models.CharField(max_length=200)
    created_date     = models.DateTimeField(default=timezone.now)
    published_date   = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.channel_name
