from rest_framework.serializers import ModelSerializer
from drf_api_logger.models import APILogsModel


class APILogsModelSerializer(ModelSerializer):
    """
    A classe pegando model APILogsModel e “traduzindo” 
    objeto do Django em formato de API

    @param1: model
    @param2: fields
    :return: retornado api E todos fields contido no model APILogsModel
    """
    class Meta:
        model = APILogsModel
        fields = '__all__'
