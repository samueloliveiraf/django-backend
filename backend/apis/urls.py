from django.urls import path
from .views import (
    get_apis_logs,
    post_filter_date,
    post_filter_contains
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
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
    ),
    
    # Interface Swagger

    path('swagger/', 
        schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'
    ),
    path('redoc/', 
        schema_view.with_ui('redoc', cache_timeout=0), 
        name='schema-redoc'
    ),
]
