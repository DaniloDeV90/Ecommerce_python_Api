

from .models import Endereco
from rest_framework import serializers
from .models import User,CarrinhoDeCompras
from .CustomError import MyCustomError



class CarrinhoCreateSerializer (serializers.ModelSerializer):
    class Meta:
        model = CarrinhoDeCompras
        fields = '__all__'




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



    def nome_sobrenome_unico (self, data ):
    

        if User.objects.filter (nome = data['nome'], sobrenome = data['sobrenome']).first ():
         raise  serializers.ValidationError ("Já existe usuario com esse nome e sobrenome")






class UserDeleteSerializer(serializers.Serializer): 
    class Meta:
        model = User
        fields = ['id']


    def deleteUser (self,data):
      try:
        print (data)

    
        user = User.objects.get (id=data)
        print(user)
        if user:
            user.delete ()
            return
    
    
      except Exception  as e:
        
        if (isinstance (e, User.DoesNotExist)):
          
            raise  serializers.ValidationError  ("Este User não existe!")
        raise serializers.ValidationError ("Erro interno")

 