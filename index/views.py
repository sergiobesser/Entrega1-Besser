from re import template
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos<h1>')

def plantilla(request):
    return render(request, 'index/plantilla.html', {})
