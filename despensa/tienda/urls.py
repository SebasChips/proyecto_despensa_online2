from django.urls import path

from . import views

urlpatterns = [
    path('tienda/', views.tienda, name ="tienda"),
    path('carro/', views.carro, name ="carro"),
    path('checkout/', views.checkout, name ="checkout"),
]