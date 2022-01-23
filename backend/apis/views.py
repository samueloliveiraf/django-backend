import json
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import APILogsModelSerializer
from drf_api_logger.models import APILogsModel
from rest_framework.decorators import api_view
import datetime


@api_view(['GET'])
def get_apis_logs(request):
    """
    A funcao esta retornando todos os logs captudado das API's

    @return: 200: a APILogsModel_REQUESTS objetos encontrados \
    com application/json mimetype.
    @raise 404: se os objetos nao foram encontrados
    """
    
    apis = APILogsModel.objects.all()
    serializer = APILogsModelSerializer(apis, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def post_filter_date(request):
    """
    A funcao esta filtrando por datas o Model APILogsModel

    @param1: startdata
    @param2: enddata
    :return: 200 a APILogsModel_REQUESTS objetos encontrados \
    com application/json mimetype.
    @raise 500: se os paramentro vindo do frontend estiver errados
    """

    json_request = json.dumps(request.data)
    json_request = json.loads(json_request)

    startdata = json_request['start_data']
    enddata = json_request['end_data']

    if startdata != None and enddata != None:
        apis = APILogsModel.objects.filter(
            added_on__range=(
            datetime.datetime.strptime(startdata,
            '%Y-%m-%d').date(),
            datetime.datetime.strptime(enddata,
            '%Y-%m-%d').date()),
        )
        serializer = APILogsModelSerializer(apis, many=True)

        return Response(serializer.data)

    else:

        return JsonResponse({
            'error_code':500, 
            'message':'Informe a data correta Ex: 2021-02-11'
            }
        )


@api_view(['POST'])
def post_filter_contains(request):
    """
    A funcao esta filtrando por datas o Model APILogsModel

    @param: string_search
    :return: 200 a APILogsModel_REQUESTS objetos encontrados \
    com application/json mimetype.
    @raise 500: se o paramentro vindo do frontend estiver errado
    """

    json_request = json.dumps(request.data)
    json_request = json.loads(json_request)

    string_search = json_request['string_search']

    if string_search!= None:
        apis = APILogsModel.objects.filter(response__contains=string_search)
        serializer = APILogsModelSerializer(apis, many=True)

        return Response(serializer.data)

    else:

        return JsonResponse({
            'error_code':500, 
            'message':'Por favor informa a palavra a ser pesquisada'
            }
        )
