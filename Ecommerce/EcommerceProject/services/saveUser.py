from django.shortcuts import get_object_or_404
from psycopg2 import IntegrityError
from rest_framework.exceptions import ValidationError
from ..serializers import CarrinhoCreateSerializer
from ..models import User

def saveUser (serializer,request):
    
     if (serializer.is_valid ()):
      serializer.save ()
      email = request.data.get ("email")
      user = get_object_or_404 (User, email=email)
      user= {'usuario': user.id}
      carrinho = CarrinhoCreateSerializer (data=user)
      if carrinho.is_valid ():
        carrinho.save ()
     else:   
        raise ValidationError ("ee")
    

