from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from mainapp.views import EventView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/events/', EventView.as_view(), name='create_event'),
    path('token/', obtain_auth_token),
]
