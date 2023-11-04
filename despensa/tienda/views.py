from django.shortcuts import render

def tienda(request):
    context = {}
    return render (request, 'tienda/tienda.html', context)

def carro(request):
    context = {}
    return render (request, 'tienda/carro.html', context)

def checkout(request):
    context = {}
    return render (request, 'tienda/checkout.html', context)