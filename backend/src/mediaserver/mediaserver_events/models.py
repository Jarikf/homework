from django.db import models


class MediaserverEvent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
