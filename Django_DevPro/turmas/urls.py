from django.urls import path
from Django_DevPro.turmas import views

app_name = 'turmas'

urlpatterns = [
    path('', views.indice, name='indice'),
]
