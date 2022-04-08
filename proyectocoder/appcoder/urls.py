from django.urls import path 
from appcoder.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('padres/', padres, name= "Padres"),
    path('hijos/', hijos, name= "Hijos"),
]