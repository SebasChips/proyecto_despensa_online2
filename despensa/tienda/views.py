from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from .models  import *
from .utils import *

def tienda(request):

    data = cartData(request)
    caritems = data['caritems']
    pedido = data['pedido']
    items = data['items']

    products = Producto.objects.all()
    context = {'products': products, 'caritems': caritems}
    return render (request, 'tienda/tienda.html', context)


def carro(request):

    data = cartData(request)
    caritems = data['caritems']
    pedido = data['pedido']
    items = data['items']


    try:
            carro= json.loads(request.COOKIES['carro'])
    except:
            carro = {}
    print ( 'Cart', carro)
    items = []
    pedido = {'get_carro_total':0, 'get_carro_productos':0 , 'shipping':False}
    caritems = pedido ['get_carro_productos']

    for i in carro:
            try:
                caritems += carro[i]["quantity"]
                product =  Producto.objects.get(id=1)
                total = (product.precio * carro[i]["quantity"])

                pedido['get_cart_total'] +=total
                pedido['get_cart_total'] +=carro[i]["quantity"]

                item = {
                    'product':{
                        'id': product.id,
                        'name': product.name,
                        'price': product.price,
                        'imageURL': product.imageURL,
                    },
                    'quantity': carro[i]["quantiy"],
                    'get_total': total,
                }
                items.append(item)

                if product.digital == False:
                    pedido['shipping'] = True
            except:
                pass

    context = {'items': items , 'order': pedido , 'caritems': caritems}

    return render(request, 'tienda/carro.html', context)


#from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def checkout(request):
    
    data = cartData(request)
    caritems = data['caritems']
    pedido = data['pedido']
    items = data['items']
        
    context = {'items': items , 'order': pedido , 'caritems': caritems}
    return render (request, 'tienda/checkout.html', context)


def updateItem (request):
    data = json.loads(request.body)
    productId = data ['productId']
    action = data ['action']

    print('action:', action)
    print('productId:', productId)

    cliente = request.user.cliente
    producto = Producto.objects.get(id = productId)
    pedido, created = Pedido.objects.get_or_create(usuario=cliente, completo=False)

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
        

        
    else:
        cliente, pedido = guestOrder(request, data)                          
    
    total = float(data['form']['total'])
    pedido.id_transaccion = id_transaccion

    if total == orden_producto.get_cart_total:
            orden_producto.complete=True
    orden_producto.save()

    if pedido.shipping == True:
            Lugar_envio.objects.create(
                cliente = cliente,
                pedido =orden_producto,
                address=data ['shipping']['address'],
                city=data ['shipping']['city'],
                state=data ['shipping']['state'],
                zipcode=data ['shipping']['zipcode'],

            )
    
    return JsonResponse('¡Pago completado!', safe =False)