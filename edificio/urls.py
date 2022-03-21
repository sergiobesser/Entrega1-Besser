from django.urls import path
from .views import consorcio, inquilino, propietario, busqueda_inquilino

urlpatterns = [
    path('propietario/', propietario, name='propietario'),
    path('inquilino/', inquilino, name='inquilino'),
    path('consorcio/', consorcio, name='consorcio'),
    path('busqueda_inquilino/', busqueda_inquilino, name='busqueda_inquilino'),
]
