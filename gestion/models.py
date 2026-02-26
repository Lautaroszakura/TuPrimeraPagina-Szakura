from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre=models.CharField(max_length=40)
    telefono=models.CharField(max_length=20)
    email=models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Local(models.Model):
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=40)
    precio=models.FloatField()
    stock=models.IntegerField()
    Proveedor=models.ForeignKey(Proveedor ,on_delete=models.CASCADE)
    local=models.ForeignKey(Local, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    