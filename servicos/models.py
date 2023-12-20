from django.db import models

# Create your models here.
class Servicos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    descrição = models.TextField()

    def __str__(self) -> str:
        return self.nome
    

class Pecas(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    quantidade = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.nome
