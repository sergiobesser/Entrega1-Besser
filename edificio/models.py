from django.db import models

# Create your models here.
#Probar clase maestra y que las 3 hereden nombre, apellido y email

class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    unidad = models.CharField(max_length=3)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class Inquilino(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    unidad = models.CharField(max_length=3)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class Consorcio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'