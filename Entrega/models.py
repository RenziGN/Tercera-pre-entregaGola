from django.db import models

# Create your models here.
class Usuarios(models.Model):
    User = models.CharField(max_length=50)
    Mail = models.EmailField(max_length=150)
    Password = models.CharField(max_length=50)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    Precio = models.FloatField(default=0)

class Ventasproducto(models.Model):
    nombreproducto = models.CharField(max_length=50)
    Cantidaddeventas = models.IntegerField()



   


