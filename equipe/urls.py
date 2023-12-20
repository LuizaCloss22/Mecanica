from django.urls import path
from . import views

app_name = 'equipe'  # Defina o namespace para sua aplicação

urlpatterns = [
    path('equipe/', views.add_equipe, name='equipes'),
    path('funcionario/', views.add_funcionario, name='funcionario'),
]
