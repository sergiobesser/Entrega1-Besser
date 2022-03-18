from django.shortcuts import render
from .forms import ConsorcioFormulario, InquilinoFormulario, PropietarioFormulario
# Create your views here.

def propietario(request):   
    form = PropietarioFormulario
    return render(request, 'edificio/propietario.html',{'form': form})

def inquilino(request):       
    form = InquilinoFormulario()
    return render(request, 'edificio/inquilino.html', {'form': form})

def consorcio(request):
    form = ConsorcioFormulario
    return render(request, 'edificio/consorcio.html',{'form': form})
