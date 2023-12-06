from django.shortcuts import render
from .models import cliente
from .models import Pedido
from .models import orden_producto
from .models import Producto
from .models import Lugar_envio
from django.http import JsonResponse
import json
import datetime

def tienda(request):

    if request.user.is_authenticated:
        # Accede directamente al campo "usuario"
        customer = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(usuario=customer, completo=False)
        items = pedido.orden_producto_set.all()
        caritems = pedido.get_carro_productos
    else:
        items = []
        pedido = {'get_carro_total':0, 'get_carro_productos':0, 'shipping':False}
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
        pedido = {'get_carro_total':0, 'get_carro_productos':0 , 'shipping':False}
        caritems = pedido ['get_carro_productos']

    context = {'items': items , 'order': pedido , 'caritems': caritems}

    return render(request, 'tienda/carro.html', context)


#from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def checkout(request):

    if request.user.is_authenticated:
        # Accede directamente al campo "usuario"
        customer = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(usuario=customer, completo=False)
        items = pedido.orden_producto_set.all()
        caritems = pedido.get_carro_productos
    else:
        items = []
        pedido = {'get_carro_total':0, 'get_carro_productos':0 , 'shipping':False}
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
    return JsonResponse('Item fue añadido', safe=False)


@csrf_exempt

def proccessOrder(request):
    id_transaccion = datetime.datetime.now().timestamp()
    data =json.loads(request.body)

    if request.user.is_authenticated:
        costumer =request.user.costumer
        pedido, created = Pedido.objects.get_or_create(usuario=cliente, completo=False)
        total = float(data['form']['total'])
        pedido.id_transaccion = id_transaccion

        if total == orden_producto.get_cart_total:
            orden_producto.complete=True
        orden_producto.save()

        if orden_producto.shipping == True:
            Lugar_envio.objects.create(
                custumer = cliente,
                order =orden_producto,
                address=data ['shipping']['address'],
                city=data ['shipping']['city'],
                state=data ['shipping']['state'],
                zipcode=data ['shipping']['zipcode'],

            )
        
    else:
        print ('El usuario no inicio sesión...')
    return JsonResponse('¡Pago completado!', safe =False)