from django.shortcuts import render

# Create your views here.

def propietario(request):
    return render(request, 'edificio/propietario.html',{})

def inquilino(request):
    return render(request, 'edificio/inquilino.html',{})

def consorcio(request):
    return render(request, 'edificio/consorcio.html',{})
