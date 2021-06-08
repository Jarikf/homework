import datetime

import django_filters
from django.utils import timezone
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import MediaserverEvent
from .serializers import MediaserverEventsSerializer
from backend.mixins import CountModelMixin


class MediaserverEventsFilter(django_filters.FilterSet):
    max_age = django_filters.NumberFilter(method='max_age_filter')

    def max_age_filter(self, queryset, name, value):
        return queryset.filter(created_at__gt=timezone.now()-datetime.timedelta(seconds=int(value)))


class MediaserverEventsViewSet(mixins.CreateModelMixin, CountModelMixin, viewsets.GenericViewSet):
    serializer_class = MediaserverEventsSerializer
    permission_classes = [AllowAny]
    queryset = MediaserverEvent.objects.all()
    filterset_class = MediaserverEventsFilter
