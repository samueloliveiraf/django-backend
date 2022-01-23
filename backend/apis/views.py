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
    A funcao esta retornando todas as Apis do Model APILogsModel

    :return: serializer.data
    """
    
    apis = APILogsModel.objects.all()
    serializer = APILogsModelSerializer(apis, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def post_filter_date(request):
    """
    A funcao esta filtrando por datas o Model APILogsModel

    :return: serializer.data
    """

    json_request = json.dumps(request.data)
    json_request = json.loads(json_request)

    startdata = json_request['startdata']
    enddata = json_request['enddata']

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
            'message':'Informe a data correta Ex: 2021-02-11'}
        )


@api_view(['POST'])
def post_filter_contains_string(request):
    """
    A funcao esta filtrando por string(Response) o Model APILogsModel
    
    :return: serializer.data
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
            'message':'Por favor informa a palavra a ser pesquisada'}
        )
