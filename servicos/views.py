from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Servicos, Pecas
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

def servicos(request):
    if request.method == 'GET':
        #servicoslist = Servicos.objects.all()
        return render(request, 'servicos.html')
    elif request.method == 'POST':
        nome_servico = request.POST.get('nome_servico')
        preco_servico = request.POST.get('preco_servico')
        descricao_servico = request.POST.get('descricao_servico')

        servico =Servicos.objects.filter(nome = nome_servico).first()

        if not servico:
            servico = Servicos(
                nome = nome_servico,
                preco = preco_servico,
                descrição = descricao_servico
            )
            servico.save()
    return render(request, 'servicos.html')

def pecas(request):
    if request.method == 'GET':
        return render(request, 'pecas.html')
    elif request.method == 'POST':
        nome_peca = request.POST.get('nome_peca')
        preco_peca = request.POST.get('preco_peca')
        estoque_peca = request.POST.get('estoque_peca')

        peca = Pecas.objects.filter(nome = nome_peca).first()

        if not peca:
            peca = Pecas(
                nome = nome_peca,
                preco = preco_peca,
                quantidade = estoque_peca
            )
            peca.save()
    return render(request, 'pecas.html')
        

