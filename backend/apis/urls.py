from django.urls import path
from .views import (
    get_apis_logs,
    post_filter_date,
    post_filter_contains
)


urlpatterns = [
    path('list-logs-apis/',
        get_apis_logs,
        name='list-logs-apis'
    ),
    path('list-logs-apis/date/',
        post_filter_date,
        name='list-logs-apis-date'
    ),
    path('list-logs-api/contains/',
        post_filter_contains,
        name='list-logs-api-contains'
    )
]
