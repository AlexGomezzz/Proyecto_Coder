from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    date_init = datetime.now()
    dict_ctx = {"title": "Inicio", "message": "Bienvenid@s" }
    return render(request, "appcoder/index.html")

def padres(request):
    return render(request, "appcoder/padres.html")

def hijos(request):
    return render(request, "appcoder/hijos.html")
