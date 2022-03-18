from django.shortcuts import redirect, render

from edificio.models import Inquilino
from .forms import ConsorcioFormulario, InquilinoFormulario, PropietarioFormulario
# Create your views here.

def propietario(request):   
    form = PropietarioFormulario
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
    form = ConsorcioFormulario
    return render(request, 'edificio/consorcio.html',{'form': form})
