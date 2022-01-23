from rest_framework.serializers import ModelSerializer
from drf_api_logger.models import APILogsModel


class APILogsModelSerializer(ModelSerializer):
    class Meta:
        model = APILogsModel
        fields = '__all__'
