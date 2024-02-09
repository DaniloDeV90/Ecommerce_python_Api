from django.db import models
from django.db.models import UniqueConstraint


class User(models.Model):
    nome = models.CharField(max_length=100 )
    sobrenome = models.TextField()
    email = models.CharField (max_length=100)
    senha = models.CharField (max_length = 40)
    class Meta:
        constraints = [
        UniqueConstraint (fields=['nome','sobrenome'], name='nome_sobrenome_unico')

    ]


    def __str__(self):
        return self.nome


class CarrinhoDeCompras (models.Model):
    produto_nome = models.CharField (max_length = 100, null=True, )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE )



class Endereco  (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE )
    Rua  = models.CharField (max_length = 100, null=False )
    cep  = models.CharField (max_length = 8, null=False)
    cidade   = models.CharField (max_length = 100, null=False)
    estado   = models.CharField (max_length = 50, null=False )
    bairro =  models.CharField (max_length = 200, null=False)