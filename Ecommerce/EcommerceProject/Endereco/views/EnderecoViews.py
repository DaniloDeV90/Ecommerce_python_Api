from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...serializers import EnderecoSerializer



@api_view(['POST'])
def criar_endereco (request):
        serializerCarrinho = EnderecoSerializer(data=request.data)
        
        if serializerCarrinho.is_valid():
            serializerCarrinho.save()
            serializerCarrinho.min_length_cep (request.data)
            return Response(serializerCarrinho.data, status=status.HTTP_201_CREATED)
        return Response(serializerCarrinho.errors, status=status.HTTP_400_BAD_REQUEST)