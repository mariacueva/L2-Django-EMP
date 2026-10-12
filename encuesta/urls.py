from django.urls import path
from . import views

app_name= 'encuesta'
urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'), 
    path('enviar', views.enviar, name='enviar'),
    
    # Calculadora de operaciones matemáticas
    path('calculadora/', views.calculadora,
     name='calculadora'),
    
    path('resultado-calculadora/',
     views.resultado_calculadora,
     name='resultado_calculadora'),
    
    # Calculadora del volumen del cilindro
    path('cilindro/', views.cilindro,
     name='cilindro'),
    
    path('resultado-cilindro/',
     views.resultado_cilindro,
     name='resultado_cilindro'),
]