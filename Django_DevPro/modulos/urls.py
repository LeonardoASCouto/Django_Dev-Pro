from django.urls import path
from Django_DevPro.modulos import views

app_name = 'modulos'

urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
]
