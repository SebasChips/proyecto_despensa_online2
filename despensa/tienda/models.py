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
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    @property
    def  imageURL(self):
     try:
        url = self.image.url
     except:
        url = ''
     return url 
      
# Modelo de Pedido
class Pedido(models.Model):
    usuario = models.ForeignKey( cliente, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    completo = models.BooleanField(default=False, null=True, blank=False)
    id_transaccion = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
    @property 

    def shipping (self):
       shipping = False
       ordenproducto = self.ordenproducto_set.all()
       for i in ordenproducto:
          if i.producto.digital == False:
             shipping = True
       return shipping

   
 


    
       
    
    @property
    def get_carro_total(self):
       orden_productos = self.orden_producto_set.all()
       total = sum([item.get_total for item in orden_productos])
       return total
    
    @property
    def get_carro_productos(self):
       orden_productos = self.orden_producto_set.all()
       total = sum([item.cantidad for item in orden_productos])
       return total

    

class orden_producto(models.Model):

    producto = models.ForeignKey( Producto , on_delete=models.SET_NULL, blank= True, null=True)
    orden = models.ForeignKey ( Pedido , on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True )
    fecha_anadida = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
       total= self.producto.precio * self.cantidad
       return total


class Lugar_envio (models.Model):
   
   usuario = models.ForeignKey(cliente, on_delete=models.SET_NULL, blank=True, null=True)
   orden = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
   direccion = models.CharField (max_length=255, null=True)
   ciudad = models.CharField (max_length=255, null=True )
   estado = models.CharField (max_length=255, null=False)
   codigo_postal = models.CharField (max_length=255, null=False)
   fecha_anadido = models.DateTimeField (auto_now_add=True)


   def __str__(self):

      return self.direccion








