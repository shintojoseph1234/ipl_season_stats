# django imports
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# REST API imports
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

# documentation view
document_view   = include_docs_urls(title='IPL_Season API', public=True)
# schema view
schema_view     = get_schema_view(title="IPL_Season API")
# swagger schema view
swagger_schema_view = get_swagger_view(title='IPL_Season API')

urlpatterns = [

    # index
    path('', views.index, name='index'),

    # REST API documentation
    path('api/', document_view),

    # csv -> database ingest
    path('ingest_csv', views.ingest_csv, name='ingest_csv'),

    # default schema view
    path('api/schema/', schema_view),

    # swagger schema view
    path('api/swagger_schema/', swagger_schema_view),

    # GET IPL season details
    path('api/search/<str:season>', views.season_stats, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
