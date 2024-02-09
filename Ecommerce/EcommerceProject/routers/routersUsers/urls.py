from django.urls import path
from  ...User.view.UserView import criar_usuario,delete
from  ...Endereco.views.EnderecoViews import criar_endereco

urlpatterns = [
    path('', criar_usuario, name='criar_usuario'),
    path ('endereco/',  criar_endereco, name='criar_endereco'),
    path ('deletar/<int:user_id>/', delete, name='deletar_usuario')
]
