from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api/polls/', include('polls.urls')),
    path('', schema_view),
]
