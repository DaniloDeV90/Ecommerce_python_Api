from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...serializers import CarrinhoCreateSerializer



@api_view(['POST'])
def criar_carrinho (request):
        serializerCarrinho = CarrinhoCreateSerializer(data=request.data)
        
        if serializerCarrinho.is_valid():
            serializerCarrinho.save()
            return Response(serializerCarrinho.data, status=status.HTTP_201_CREATED)
        return Response(serializerCarrinho.errors, status=status.HTTP_400_BAD_REQUEST)