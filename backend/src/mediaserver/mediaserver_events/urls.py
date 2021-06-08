from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MediaserverEventsViewSet

router = DefaultRouter()
router.register('mediaserver-events', MediaserverEventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
