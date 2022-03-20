from django.shortcuts import redirect, render

from edificio.models import Consorcio, Inquilino
from .forms import ConsorcioFormulario, InquilinoFormulario, PropietarioFormulario
# Create your views here.

def propietario(request):   
    if request.method =='POST':
        form = PropietarioFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            propietario = Inquilino(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], unidad=data['unidad'], habita_la_unidad=data['habita_la_unidad'])
            propietario.save()
            return redirect('index')
    
    form = PropietarioFormulario()
    return render(request, 'edificio/propietario.html',{'form': form})


def inquilino(request):
    if request.method == 'POST':
        form = InquilinoFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            inquilino = Inquilino(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], unidad=data['unidad'])
            inquilino.save()
            return redirect('index')
            
    form = InquilinoFormulario()
    return render(request, 'edificio/inquilino.html', {'form': form})


def consorcio(request):
    if request.method == 'POST':
        form = ConsorcioFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            consorcio = Consorcio(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            consorcio.save()
            return redirect('index')
        
    form = ConsorcioFormulario()
    return render(request, 'edificio/consorcio.html',{'form': form})
