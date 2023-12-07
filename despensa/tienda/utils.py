import json
from . models import *

def cookieCart(request):
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
    return {'caritems':caritems,'pedido': pedido, 'items':items}

def  cartData(request):
        if request.user.is_authenticated:
            # Accede directamente al campo "usuario"
            customer = request.user.cliente
            pedido, created = Pedido.objects.get_or_create(usuario=customer, completo=False)
            items = pedido.orden_producto_set.all()
            caritems = pedido.get_carro_productos
        else:
            cookieData = cookieCart()
            caritems = cookieData['caritems']
            pedido = cookieData['pedido']
            items = cookieData['items']
        return {'caritems':caritems,'pedido': pedido, 'items':items}


def guestOrder (request, data):
    print ('El usuario no inicio sesión...')

    print('COOKIES: ', request.COOKIES)
    nam = data['forma']['name']
    email = data['form' ['email']]

    cookieData = cookieCart(request)
    items = cookieData['items']

    cliente,created = Cliente.objects.get_or_create(
        email=email,
        )
    costumer.name = name
    Cliente.save()

    pedido = Pedido.objects.create(
             cliente=cliente,
             complete = False,
        )

    for item in items:
            producto = Producto.objects.get(id=item['producto']['id'])
                                            
            ordenProducto= orden_producto.create(
                 producto= producto,
                 pedido = pedido,
                 quantity = item['quantity']
            )  

    return cliente, pedido