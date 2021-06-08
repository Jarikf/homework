from rest_framework.serializers import ModelSerializer
from .models import MediaserverEvent


class MediaserverEventsSerializer(ModelSerializer):
    class Meta:
        model = MediaserverEvent
        fields = '__all__'
        read_only_fields = ['created_at']
