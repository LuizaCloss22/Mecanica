from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from clientes.models import Carro, Cliente
from equipe.models import Equipe
from servicos.models import Servicos, Pecas
from .models import Requisicao
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def pedido(request):
    if request.method == 'GET':
        equipe_list = Equipe.objects.all()
        return render(request, 'pedido.html', {'equipes':equipe_list})
    elif request.method == 'POST':
        descricao = request.POST.get('descricao_servico')
        data_inicio = request.POST.get('data')
        carro_id = request.POST.get('id_carro')
        print(carro_id)
        equipe_id = request.POST.get('equipe')
        equipe_selecionada = Equipe.objects.get(pk=equipe_id)

        requisicao = Requisicao(
            descricao = descricao,
            data_inicio = data_inicio,
            carro_id = carro_id,
            equipe_id = equipe_id,
        )
        requisicao.save()
        return HttpResponse('salvou requisição')

def achar_carro(request):
    if request.method == 'POST':
        placa = request.POST.get('placa')
        try:
            carro = get_object_or_404(Carro, placa=placa)
                        
            id_carro = json.loads(serializers.serialize('json', [carro]))[0]['pk']

            cliente = Cliente.objects.filter(nome = carro.cliente).first()
            cliente_nome = cliente.nome
            cliente_id = json.loads(serializers.serialize('json', [cliente]))[0]['pk']
            
            
            carro_info = {
                'id' : id_carro,
                'cliente': cliente_nome,
                'cliente_id': cliente_id,
                'carro': carro.carro,
                'ano': carro.ano,
            }
            return JsonResponse({'carro': carro_info})
        except Carro.DoesNotExist:
            carro_info = {
                'status': 'erro'
            }
            return JsonResponse({'status':carro_info})
        
def calendario(request):
    if request.method == 'GET':
        reqlist = Requisicao.objects.all()
        listaCompleta = []
        listaIncompleta = []
        for requisicao in reqlist:
            if requisicao.data_entrega is None:
                listaIncompleta.append(requisicao)
            else:
                listaCompleta.append(requisicao)

        return render(request, 'calendario.html', {'requisiçõesIncompletas': listaIncompleta, 'requisiçõesCompletas': listaCompleta})

@csrf_exempt
def update(request, id):
    requisição = Requisicao.objects.filter(id = id).first()
    carro = requisição.carro
    equipe = requisição.equipe

    pecas = Pecas.objects.all()
    servicos = Servicos.objects.all()

    jsonRequisição = json.loads(serializers.serialize('json',[requisição]))[0]['fields']
    idRequisição = json.loads(serializers.serialize('json',[requisição]))[0]['pk']

    data = {'id': idRequisição, 'fields':jsonRequisição}
    print(jsonRequisição)

    return render(request, 'update.html', {'carro': carro, 'equipe':equipe, 'data':data, 'pecas':pecas, 'servicos': servicos})

def finalizar(request):
    if request.method == "POST":
        try:
            id = request.POST.get('id')
            placacarro = request.POST.get('carro')
            carro = Carro.objects.filter(placa = placacarro).first()
            data_inicio = request.POST.get('data_inicio')
            equipe = request.POST.get('equipe')
            descricao = request.POST.get('descricao')
            data_entrega = request.POST.get('data_entrega')
            id_peca = request.POST.get('peca')
            quantidade = request.POST.get('quantidade')
            id_servico = request.POST.get('servico')

            if quantidade is not None:
                quantidade = int(quantidade)
            else:
                quantidade = 1  # Defina um valor padrão ou trate de acordo com a lógica do seu sistema

            peca = Pecas.objects.get(id=id_peca)
            servico = Servicos.objects.get(id=id_servico)

            valor_peca = peca.preco
            valor_servico = servico.preco

            valor_total = (valor_peca * quantidade) + valor_servico

            requisicao = get_object_or_404(Requisicao, id=id)
            requisicao.carro = carro
            requisicao.descricao = descricao
            requisicao.data_inicio = data_inicio
            requisicao.data_entrega = data_entrega
            requisicao.servico = servico
            requisicao.peca = peca
            requisicao.valor_final = valor_total
            requisicao.save()

            return HttpResponse("Pedido finalizado com sucesso!")
        except Exception as e:
            print("Erro ao finalizar pedido:", str(e))
            return HttpResponse("Ocorreu um erro ao finalizar o pedido. Por favor, tente novamente.")
    else:
        return HttpResponse("Método não permitido para esta rota.")
