from django.urls import path
from .views import consorcio, inquilino, propietario

urlpatterns = [
    path('propietario/', propietario, name='propietario'),
    path('inquilino/', inquilino, name='inquilino'),
    path('consorcio/', consorcio, name='consorcio'),
]
