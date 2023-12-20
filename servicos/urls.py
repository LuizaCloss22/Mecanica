from django.urls import path
from . import views

app_name = 'servicos'

urlpatterns = [
    path('servicos/', views.servicos, name='servicos'),
    path('pecas/', views.pecas, name='pecas'),
]