from django.contrib import admin

from .models import Consorcio, Inquilino, Propietario

# Register your models here.

admin.site.register(Propietario)
admin.site.register(Inquilino)
admin.site.register(Consorcio)