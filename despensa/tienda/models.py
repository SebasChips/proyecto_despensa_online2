from django.db import models



# Modelo de Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    dirección = models.CharField(max_length=255)
    teléfono = models.CharField(max_length=20)

# Modelo de Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripción = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen_url = models.CharField(max_length=255)

# Modelo de Categoría
class Categoría(models.Model):
    nombre = models.CharField(max_length=255)

# Modelo de Pedido
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)