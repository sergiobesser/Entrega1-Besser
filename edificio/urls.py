from django.urls import path
from .views import consorcio, index, inquilino, propietario

urlpatterns = [
    path('', index, name='index'),
    path('propietario/', propietario, name='propietario'),
    path('inquilino/', inquilino, name='inquilino'),
    path('consorcio/', consorcio, name='consorcio'),
]
