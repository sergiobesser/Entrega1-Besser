from django import forms

class PropietarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    unidad = forms.CharField(max_length=3)
    habita_la_unidad = forms.BooleanField(required=False)
    
    
class InquilinoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    unidad = forms.CharField(max_length=3)
    
    
class ConsorcioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()