from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  ...serializers import UserCreateSerializer,UserDeleteSerializer



@api_view(['POST'])
def  criar_usuario(request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid ():
            print ("valido")
            serializer.nome_sobrenome_unico (request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view (['DELETE'])
def delete  (request, user_id):
  try:

    serializer = UserDeleteSerializer (data= {user_id: user_id})
    
    if serializer.is_valid ():
   
        serializer.deleteUser (user_id)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)

  except Exception as e:
    return Response  (e, status=status.HTTP_406_NOT_ACCEPTABLE)
    