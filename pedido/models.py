from django.db import models
from clientes.models import Carro, Cliente
from equipe.models import Equipe
from servicos.models import Servicos, Pecas

# Create your models here
class Requisicao(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(max_length=1000)
    data_inicio = models.DateField()
    data_entrega = models.DateField(null=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    servico = models.ForeignKey(Servicos, on_delete=models.SET_NULL, null=True)
    pecas = models.ForeignKey(Pecas, on_delete=models.SET_NULL, null=True)
    valor_final = models.DecimalField(decimal_places=2, max_digits=8, null=True)