from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework.response import Response


class CountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class CountModelMixin:
    @action(detail=False)
    @swagger_auto_schema(responses={200: CountSerializer()})
    def count(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return Response({
            'count': queryset.count()
        })
