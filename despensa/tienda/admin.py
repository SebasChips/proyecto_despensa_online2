from django.contrib import admin

# Register your models here.
from .models import*


admin.site.register(cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(orden_producto)
admin.site.register(Lugar_envio)
