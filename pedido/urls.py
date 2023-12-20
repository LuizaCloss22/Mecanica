from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'pedido'

urlpatterns = [
    path('pedido', views.pedido, name="pedido"),
    path('achar_carro/', views.achar_carro, name="carro"),
    path('calendario/', views.calendario, name='calendario'),
    path('update/<int:id>', views.update, name="update"),
    path('finalizar/', views.finalizar, name="finalizar")
]