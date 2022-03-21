from django.shortcuts import redirect, render

from edificio.models import Consorcio, Inquilino, Propietario
from .forms import ConsorcioFormulario, InquilinoFormulario, PropietarioFormulario, BusquedaInquilino
# Create your views here.

def propietario(request):   
    if request.method =='POST':
        form = PropietarioFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            propietario = Propietario(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], unidad=data['unidad'])
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


def busqueda_inquilino(request):
    inquilinos = []
    nombre_a_buscar = request.GET.get('nombre', None)
    if nombre_a_buscar is not None:
        inquilinos = Inquilino.objects.filter(nombre__icontains=nombre_a_buscar)
    # else:
    #     inquilinos = Inquilino.objects.all()
    
    form = BusquedaInquilino()
    return render(request, 'edificio/busqueda_inquilino.html', {'form': form, 'inquilinos': inquilinos})
