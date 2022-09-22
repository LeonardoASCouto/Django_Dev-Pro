from django.urls import path
from Django_DevPro.base.views import home

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
]
