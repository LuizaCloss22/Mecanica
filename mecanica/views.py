from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from clientes.models import Cliente
from servicos.models import Servicos, Pecas

def start(request):
    return render (request, 'start.html')

def listas(request):
    clientes = Cliente.objects.all()
    servico = Servicos.objects.all().order_by('preco')
    peca = Pecas.objects.all().order_by('preco')

    return render(request, 'listas.html', {'clientes':clientes, 'serviços':servico, 'pecas':peca})