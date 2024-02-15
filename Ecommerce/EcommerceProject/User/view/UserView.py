from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from django.db.utils import IntegrityError
from  ...models import User, CarrinhoDeCompras, ItemDeCarrinho,Categoria, Produto
from  ...serializers import UserCreateSerializer,CarrinhoSerializer, ItemDeCarrinho, ProdutosSerializer, CategoriaSerializer, ItensSerializer,EnderecoSerializer
from rest_framework.views import APIView
from ...EnumResponseRequest import HttpStatus


class Createendereco (APIView):

  def post (self,request):
    try:
     idUser = request.session.get ("userid")
    
     data = request.data.copy()
     data['usuario']= idUser
     
     enderecoSerializer = EnderecoSerializer (data=data)
     if enderecoSerializer.is_valid ():
        enderecoSerializer.save ()
     else:
        raise IntegrityError ()
     

    
     return  Response ("endereco criado")
      
    except Exception as e:
        if (isinstance (e, IntegrityError)):
          return Response ("Endereco ja cadastrado!", status=HttpStatus.CONFLITO.value)
        return Response (e)

class Create_User (APIView):


 def post  (self,request):
  try:
    print (request.data)
    serializer = UserCreateSerializer (data=request.data)
    if (serializer.is_valid ()):
      serializer.save ()
      email = request.data.get ("email")
      user = get_object_or_404 (User, email=email)
      user= {'usuario': user.id}
      carrinho = CarrinhoSerializer (data=user)
      if carrinho.is_valid ():
        carrinho.save ()
      return Response ("Usuario criado!")
      
    raise IntegrityError ()
  except Exception as e:
        if (isinstance (e, IntegrityError)):
          return Response ("Este úsuario ja existe!")
        return Response (e)


    
class Account (APIView):
  def delete (self,request,user_id):
 
    user = get_object_or_404 (User, id=user_id)

    user.delete ()

    return Response ("Usuario apagado!")

class Login (APIView):
    def  post (self,request):
       try:
        print("oi")
        email = request.data.get ("email")
        senha = request.data.get ("senha")
        user = get_object_or_404(User, email=email,senha=senha)
        carrinho = get_object_or_404 (CarrinhoDeCompras, usuario=user.id )
        request.session['userid'] = user.id
        request.session['carrinhoid'] = carrinho.id
        return Response( "logado!", status=status.HTTP_200_OK)
       except Exception as e:
        return Response  ("erro ae")




class FindUser(APIView):
    def get(self, request):
        try:
            
           
            id_user = request.session.get ("userid")

            user = User.objects.get (id=id_user)
            
          
      
        
  
        
         
            return Response({'nome': user.nome,'sobrenome':user.sobrenome, 'email': user.email})
            
        except Exception as e:
            return Response("ERRO: " + str(e))

class CreateProduct(APIView):
    def post(self, request):
        try:
            # Imprime os dados recebidos para depuração
            print(request.data)
            # Inicializa o serializer com os dados recebidos
            createProdutoSerializer = ProdutosSerializer(data=request.data)
            # Verifica se os dados são válidos
            if createProdutoSerializer.is_valid():
                # Salva o Produto sem cometer no banco para adicionar as categorias depois
                produto = createProdutoSerializer.save()
                # Obtém os IDs das categorias a partir dos dados da requisição
                categorias_ids = request.data.get('categoriaId', [])
                # Itera sobre cada ID de categoria, obtém o objeto Categoria correspondente e adiciona ao produto
                for categorias_id in categorias_ids:
                    categoria = Categoria.objects.get(id=categorias_id)
                    produto.categoriaId.add(categoria)
                # Confirma as alterações no banco de dados
                produto.save()
                # Retorna uma resposta de sucesso
                return Response("Produto criado com sucesso!")
            else:
                # Retorna os erros de validação
                return Response(createProdutoSerializer.errors)
        except Exception as e:
            # Retorna a exceção capturada como resposta
            return Response(str(e))

class CreateCategory (APIView):
  def post(self,request):
    try:
     print(request.data)
     createCategoriaSerializer = CategoriaSerializer (data=request.data)
     if createCategoriaSerializer.is_valid ():
        createCategoriaSerializer.save ()
        return Response ("Categoria criada!")
    except Exception as e:
      return Response ("Erro ae")




class CreateItems (APIView):
  def post (self,request):
    try:


      data = request.data.copy()
      itensSerializer = ItensSerializer (data=data)
      if itensSerializer.is_valid():
       itensSerializer.save ()
       return Response ("produto cadastrado")
      return Response("erro ae")
    except Exception as e:
      return Response ("Erro ae")


class FindCarrinho (APIView):
  def get (self,request):
      
        idcarrinho = request.session.get ("carrinhoid")
        item_carrinho = ItemDeCarrinho.objects.filter(carrinho_id=idcarrinho)
        produtos_associados = []      
        for item in item_carrinho:
          produtos_info = {
              "produto": item.produto.nome,
              "categorias": item.produto.get_categoria_nome (),
              "quantidade": item.quantidade,
              "preco": item.produto.preco
            }
          produtos_associados.append (produtos_info)

        
        return  Response ({"carrinho":produtos_associados})

