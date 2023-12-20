from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start, name='main' ),
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('servicos/', include('servicos.urls')),
    path('equipe/', include('equipe.urls')),
    path('pedido/', include('pedido.urls')),
    path('lista/', views.listas, name='listas')
]
