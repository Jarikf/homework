import datetime

import requests
from django.conf import settings
from django.utils import timezone
from requests.auth import HTTPBasicAuth

from mediaserver.mediaserver_events.models import MediaserverEvent


def _post(url, *args, **kwargs):
    requests.post(settings.MEDIASERVER_ADDRESS + url, *args, **kwargs,
                  verify=False,
                  auth=HTTPBasicAuth(settings.MEDIASERVER_USER, settings.MEDIASERVER_PASSWORD))


def _createEvent(**kwargs):
    _post('/api/createEvent', json=kwargs)


def report_last_minute_actions():
    one_minute_ago = timezone.now()-datetime.timedelta(seconds=60)
    count = MediaserverEvent.objects.filter(created_at__gt=one_minute_ago).count()
    _createEvent(caption=f'{count} events occurred last minute')
