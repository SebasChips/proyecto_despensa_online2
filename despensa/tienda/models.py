from django.db import models
from django.contrib.auth.models import User


# Modelo de Usuario
class cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True , blank=True)
    nombre = models.CharField(max_length=255, null=True )
    email = models.EmailField(max_length=255 ,null=True)
    

    def __str__(self):
        return self.nombre


# Modelo de Producto
class Producto(models.Model):

    nombre = models.CharField(max_length=255, null=True)
    precio = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False )


    def __str__(self):
        return self.nombre


# Modelo de Pedido
class Pedido(models.Model):
    usuario = models.ForeignKey( cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    completo = models.BooleanField(default=False, null=True, blank=False)
    id_transaccion = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    

class orden_producto(models.Model):

    producto = models.ForeignKey( Producto , on_delete=models.SET_NULL, blank= True, null=True   )
    orden = models.ForeignKey ( Pedido , on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True )
    fecha_anadida = models.DateTimeField(auto_now_add=True)


class Lugar_envio (models.Model):
   
   usuario = models.ForeignKey(cliente, on_delete=models.CASCADE, blank=True, null=True)
   orden = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
   direccion = models.CharField (max_length=255, null=True)
   ciudad = models.CharField (max_length=255, null=True )
   estado = models.CharField (max_length=255, null=False)
   codigo_postal = models.CharField (max_length=255, null=False)
   fecha_anadido = models.DateTimeField (auto_now_add=True)


def __str__(self):
        return self.direccion








