from django.shortcuts import render
from .models import cliente
from .models import Pedido
from .models import orden_producto
from .models import Producto
from .models import Lugar_envio
from django.http import JsonResponse
import json


def tienda(request):

    if request.user.is_authenticated:
        # Accede directamente al campo "usuario"
        customer = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(usuario=customer, completo=False)
        items = pedido.orden_producto_set.all()
        caritems = pedido.get_carro_productos
    else:
        items = []
        pedido = {'get_carro_total':0, 'get_carro_productos':0}
        caritems = pedido ['get_carro_productos']

    products = Producto.objects.all()
    context = {'products': products, 'caritems': caritems}
    return render (request, 'tienda/tienda.html', context)


def carro(request):

    if request.user.is_authenticated:
        # Accede directamente al campo "usuario"
        customer = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(usuario=customer, completo=False)
        items = pedido.orden_producto_set.all()
        caritems = pedido.get_carro_productos
    else:
        items = []
        pedido = {'get_carro_total':0, 'get_carro_productos':0 }
        caritems = pedido ['get_carro_productos']

    context = {'items': items , 'order': pedido , 'caritems': caritems}

    return render(request, 'tienda/carro.html', context)



#def carro(request):
    items = []

    if request.user.is_authenticated:
        # Usa getattr para obtener el cliente o establecer None si no existe
        customer = getattr(request.user, 'cliente', None)
        
        if customer:
            order, created = Pedido.objects.get_or_create(usuario=customer, completo=False)
            items = order.orden_producto_set.all()

    context = {'items': items}
    return render(request, 'tienda/carro.html', context)






#from django.shortcuts import get_object_or_404


#def carro(request):

   

    if request.user.is_authenticated:

        cliente = getattr(request.user, 'cliente', None)
        
        if cliente:
            pedido, created = Pedido.objects.get_or_create(usuario=cliente, completo=False)
            items = pedido.orden_producto_set.all()
      
        items = []

        context = {'items': items}
        return render(request, 'tienda/carro.html', context)

#def carro(request):
    if request.user.is_authenticated:
        # Obtener el cliente asociado al usuario autenticado
        cliente_actual = cliente.objects.get(usuario=request.user)

        # Obtener o crear un pedido para el cliente
        order, created = Pedido.objects.get_or_create(usuario=customer, completo=False)

        # Obtener los productos en el pedido
        items = pedido.orden_producto_set.all()
    else:
        items = []

    context = {'items': items}
    return render(request, 'tienda/carro.html', context)

#def carro(request):
    items = []

    if request.user.is_authenticated:
        cliente = getattr(request.user, 'cliente', None)
        
        if cliente:
            try:
                pedido, created = Pedido.objects.get_or_create(usuario=cliente, completo=False)
                items = pedido.orden_producto_set.all()
            except Pedido.DoesNotExist:
                # Hacer algo si el pedido no existe (opcional)
                pass
            except Exception as e:
                # Manejar la excepción de manera adecuada
                print(f"Error al obtener el pedido: {e}")

    context = {'items': items}
    return render(request, 'tienda/carro.html', context)
     

def checkout(request):

    if request.user.is_authenticated:
        # Accede directamente al campo "usuario"
        customer = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(usuario=customer, completo=False)
        items = pedido.orden_producto_set.all()
        caritems = pedido.get_carro_productos
    else:
        items = []
        pedido = {'get_carro_total':0, 'get_carro_productos':0}
        caritems = pedido ['get_carro_productos']
        
    context = {'items': items , 'order': pedido , 'caritems': caritems}
    return render (request, 'tienda/checkout.html', context)


def updateItem (request):
    data = json.loads(request.body)
    productId = data ['productId']
    action = data ['action']

    print('action:', action)
    print('productId:', productId)

    customer = request.user.cliente
    producto = Producto.objects.get(id = productId)
    pedido, created = Pedido.objects.get_or_create(usuario=customer, completo=False)

    ordenproducto, created = orden_producto.objects.get_or_create( orden = pedido , producto = producto)

    if action == 'add' :
        ordenproducto.cantidad = (ordenproducto.cantidad + 1)
    elif action == 'remove':
        ordenproducto.cantidad = (ordenproducto.cantidad - 1)

    
    ordenproducto.save()

    if ordenproducto.cantidad <= 0:
        ordenproducto.delete()
    return JsonResponse('Item was added', safe=False)