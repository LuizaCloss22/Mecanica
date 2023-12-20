from django.db import models

# Create your models here.
class Equipe(models.Model):
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=12)
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nome