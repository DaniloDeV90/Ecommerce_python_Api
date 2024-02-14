from django.urls import path
from  ...User.view.UserView import Create_User,Account,Login,FindUser,CreateProduct,CreateCategory,CreateItems, FindCarrinho


urlpatterns = [
    path('', Create_User.as_view (), name='criar_usuario'),
    path  ('find/',FindUser.as_view (), name='trazer_usuario'),
    path ('createProduct/',CreateProduct.as_view (), name="criarproduto" ),
    path ('deletar/<int:user_id>/', Account.as_view (), name='deletar_usuario'),
    path ("cadastraritems/", CreateItems.as_view (), name ='criar itens'),
    path ('categoria/',CreateCategory.as_view (), name='criar_categoria' ),
    path  ('login/', Login.as_view (), name='login' ),
    path ('findcarrinho/',FindCarrinho.as_view (), name='trazer_carrrinho')
]
