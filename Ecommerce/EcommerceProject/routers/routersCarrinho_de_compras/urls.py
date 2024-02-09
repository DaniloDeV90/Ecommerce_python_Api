from django.urls import path
from  ...Carrinho_de_compras.view.CarrinhoView import criar_carrinho

urlpatterns = [
    path('', criar_carrinho , name='criar_carrinho'),
    
]
