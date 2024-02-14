from django.db import models
from django.db.models import UniqueConstraint







   




class User(models.Model):
    nome = models.CharField(max_length=100 )
    sobrenome = models.TextField() 
    email = models.CharField (max_length=100, unique=True)
    senha = models.CharField (max_length = 40)





    def __str__(self):
        return self.nome



class Categoria  (models.Model):
    nome = models.CharField (max_length = 100, null=False) 


class Produto (models.Model):

    nome  = models.CharField (max_length = 100, null=False )
    categoriaId = models.ManyToManyField (Categoria)
def __str__(self):
        return f"Item: {self.nome} (Quantidade: {self.quantidade})"

def get_categoria_nome(self):
        return f"Item: {self.nome} (Quantidade: {self.categoriaId.values_list ('nome', flat=True)})"




class CarrinhoDeCompras (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE )




class ItemDeCarrinho(models.Model):
    carrinho = models.ForeignKey(CarrinhoDeCompras, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

def __str__(self):
        return f"Item: {self.produto.nome} (Quantidade: {self.quantidade})"

class Endereco  (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE )
    Rua  = models.CharField (max_length = 100, null=False )
    cep  = models.CharField (max_length = 8, null=False)
    cidade   = models.CharField (max_length = 100, null=False)
    estado   = models.CharField (max_length = 50, null=False )
    bairro =  models.CharField (max_length = 200, null=False)






