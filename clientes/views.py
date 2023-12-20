from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Carro
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

def clientes(request):
    if request.method == 'GET':
        clienteslist = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes' : clienteslist})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf).first()

        if not cliente:
            cliente = Cliente(
                nome=nome,
                sobrenome=sobrenome,
                email=email,
                cpf=cpf
            )
            cliente.save()


        for carro, placa, ano in zip(carros, placas, anos):
            try:
                print(carro, placa, ano)
                carro = Carro(
                    carro=carro, 
                    placa=placa, 
                    ano=ano, 
                    cliente=cliente
                )
                carro.save()
            except Exception as e:
                print("Erro no cadastro de veículo", str(e))
        return render(request, 'start.html')

def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.get(id=id_cliente)
    jsonCliente = json.loads(serializers.serialize('json', [cliente]))[0]['fields']
    cliente_id = json.loads(serializers.serialize('json', [cliente]))[0]['pk']

    carros = Carro.objects.filter(cliente=cliente)
    jsonCarros = json.loads(serializers.serialize('json', carros))
    jsonCarros = [{'id': carro['pk'], 'fields': carro['fields'], } for carro in jsonCarros]
    data = {'cliente_id': cliente_id, 'cliente': jsonCliente, 'carros': jsonCarros}
    
    return JsonResponse(data)

@csrf_exempt
def update_carro(request, id):
    nome_carro = request.POST.get('carro')
    placa_carro = request.POST.get('placa')
    ano_carro = request.POST.get('ano')

    carro = Carro.objects.get( id = id )
    list_carros = Carro.objects.filter(placa = placa_carro).exclude( id = id )
    if list_carros.exists():
        return HttpResponse('Este número de placa já existe!')
    else:
        carro.carro = nome_carro
        carro.placa = placa_carro
        carro.ano = ano_carro

        carro.save()
    return HttpResponse("Dados alterados com sucesso")

def excluir_carro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    except:
        # TODO: Exibir mensagem de erro
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    
def update_cliente(request, id):
    corpo = json.loads(request.body)
    nome = corpo['nome']
    sobrenome = corpo['sobrenome']
    cpf = corpo['cpf']
    email = corpo['email']

    cliente = get_object_or_404(Cliente, id=id)
    try:
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.save()
        return JsonResponse({'status': '200','nome':nome, 'sobrenome':sobrenome,'email':email,'cpf':cpf})
    except:
        return JsonResponse({'status': '500'})


    return HttpResponse({'teste':'teste'})