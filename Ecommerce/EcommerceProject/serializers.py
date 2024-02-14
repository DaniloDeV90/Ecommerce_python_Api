

from .models import Categoria, Endereco
from rest_framework import serializers
from .models import User,CarrinhoDeCompras, ItemDeCarrinho, Produto






class EnderecoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

    def min_length_cep (self,data):
        if ( len (data['cep']) < 8):
            raise serializers.ValidationError ("CEP INVÁLIDO!")





class UserCreateSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'





class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields =  ['senha','email']



class UserDeleteSerializer(serializers.Serializer): 
    class Meta:
        model = User
        fields = ['id']


class CarrinhoSerializer (serializers.ModelSerializer):
    class Meta:
        model = CarrinhoDeCompras
        fields = '__all__'


 

class ProdutosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
def get_categoria_nome (self,instance):
    return instance.get_categoria_nome()



class ItensSerializer (serializers.ModelSerializer):
    class Meta:
        model = ItemDeCarrinho
        fields = '__all__'

        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

    