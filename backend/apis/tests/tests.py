from rest_framework import status
from rest_framework.test import APITestCase
from drf_api_logger.models import APILogsModel


class ApisTestCase(APITestCase):

    def setUp(self):
        """
        A funcao esta criando um modelo APILogsModel

        @param1: execution_time
        @param2: api
        @param3: client_ip_address
        @param4: headers
        @param5: headers
        @param6: body
        @param7: method
        @param8: response
        @param9: status_code
        @param10: added_on
        """
        APILogsModel.objects.create(
            execution_time='0.05517',
            api='http://localhost:8000/api/list-logs-apis/',
            client_ip_address='127.0.0.1',
            headers='"HOST": "localhost:8000","CONNECTION": "keep-alive","SEC_CH_UA": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"","AUTHORIZATION": "Bearer","SEC_CH_UA_MOBILE": "?0","USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36","SEC_CH_UA_PLATFORM": "\"Linux\"","ACCEPT_LANGUAGE": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"',
            body='',
            method='GET',
            response='"id": 1,"added_on": "2022-01-22T23:03:49.653616-03:00","api": "http://localhost:8000/api/list-logs-apis/","headers": "{\n \"HOST\": \"localhost:8000\",\n \"CONNECTION\": \"keep-alive\",\n \"SEC_CH_UA\": \"\\\" Not;A Brand\\\";v=\\\"99\\\", \\\"Google Chrome\\\";v=\\\"97\\\", \\\"Chromium\\\";v=\\\"97\\\"\",\n \"AUTHORIZATION\": \"Bearer\",\n \"SEC_CH_UA_MOBILE\": \"?0\",\n \"USER_AGENT\": \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36\",\n \"SEC_CH_UA_PLATFORM\": \"\\\"Linux\\\"\",\n \"ACCEPT\": \"*/*\",\n \"ORIGIN\": \"http://localhost:3000\",\n \"SEC_FETCH_SITE\": \"same-site\",\n \"SEC_FETCH_MODE\": \"cors\",\n \"SEC_FETCH_DEST\": \"empty\",\n \"REFERER\": \"http://localhost:3000/\",\n \"ACCEPT_ENCODING\": \"gzip, deflate, br\",\n \"ACCEPT_LANGUAGE\": \"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7\"\n}","body": "","method": "GET","client_ip_address": "127.0.0.1","status_code": 200,"execution_time": "0.01544"',
            status_code='200',
            added_on='2012-09-04 06:00:00.000000-08:00'
        )


    def test_create_new_api_logs_model(self):
        """
        A funcao esta certificando de que esta sendo 
        criado o modelo APILogsModel

        @param1: api
        """
        api = APILogsModel.objects.get(api='http://localhost:8000/api/list-logs-apis/')
        self.assertEqual(api.__str__(), 'http://localhost:8000/api/list-logs-apis/')


    def test_api_model_get(self):
        """
        A funcao esta certificando de que esta sendo 
        retornando todos os modelo APILogsMode

        @param1: response
        """
        response = APILogsModel.objects.all()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
