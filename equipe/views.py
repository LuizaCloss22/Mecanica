from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Equipe, Funcionario
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def add_equipe(request):
    if request.method == 'GET':
        return render(request, 'equipe.html')
    elif request.method == 'POST':
        nome_equipe = request.POST.get('nome')
        especialidade_equipe = request.POST.get('especialidade')


        equipe = Equipe.objects.filter(nome = nome_equipe).first()

        if not equipe:
            equipe = Equipe(
                nome = nome_equipe,
                especialidade = especialidade_equipe
            )
            equipe.save()
        return render(request, 'equipe.html')

def add_funcionario(request):
    if request.method == 'GET':
        equipesList = Equipe.objects.all()
        return render(request, 'funcionario.html', {'equipes' : equipesList})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        equipe_id = request.POST.get('equipe')
        equipe_selecionada = Equipe.objects.get(pk=equipe_id)



        funcionario = Funcionario.objects.filter(cpf = cpf).first()

        if not funcionario:
            funcionario = Funcionario(
                nome = nome,
                sobrenome = sobrenome,
                email = email,
                cpf = cpf,
                equipe = equipe_selecionada
            )
            funcionario.save()
        equipesList = Equipe.objects.all()
        return render(request, 'funcionario.html', {'equipes' : equipesList})