import uuid

from django.db import models
from django.contrib.auth.models import User


class EventType(models.Model):
    name = models.CharField(max_length=256, unique=True)

    class Meta:
        ordering = ['id']


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    info = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
