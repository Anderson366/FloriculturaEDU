"""Floricultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cliente.views import home

from cliente.views import lista_cliente
from cliente.views import lista_funcionario
from cliente.views import lista_produto
from cliente.views import lista_venda

from cliente.views import cadastrar_cliente
from cliente.views import cadastrar_funcionario
from cliente.views import cadastrar_produto
from cliente.views import cadastrar_venda

from cliente.views import atualizar_cliente
from cliente.views import atualizar_funcionario
from cliente.views import atualizar_produto
from cliente.views import atualizar_venda

from cliente.views import deletar_cliente
from cliente.views import deletar_funcionario
from cliente.views import deletar_produto
from cliente.views import deletar_venda


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('lista_cliente/', lista_cliente, name='lista_cliente'),
    path('lista_funcionario/', lista_funcionario, name='lista_funcionario'),
    path('lista_produto/', lista_produto, name='lista_produto'),
    path('lista_venda/', lista_venda, name='lista_venda'),

    path('cadastrar_cliente/', cadastrar_cliente, name='Cadastro Cliente'),
    path('cadastrar_funcionario/', cadastrar_funcionario, name='Cadastro Funcionario'),
    path('cadastrar_produto/', cadastrar_produto, name='Cadastro Produto'),
    path('cadastrar_venda/', cadastrar_venda, name='Cadastro Venda'),

    path('atualizar_cliente/<int:pk>', atualizar_cliente, name='Atualizar Cliente'),
    path('atualizar_funcionario/<int:pk>', atualizar_funcionario, name='Atualizar Funcionario'),
    path('atualizar_produto/<int:pk>', atualizar_produto, name='Atualizar Produto'),
    path('atualizar_venda/<int:pk>', atualizar_venda, name='Atualizar Venda'),

    path('deletar_cliente/<int:pk>', deletar_cliente, name='Deletar Cliente'),
    path('deletar_funcionario/<int:pk>', deletar_funcionario, name='Deletar Funcionario'),
    path('deletar_produto/<int:pk>', deletar_produto, name='Deletar Produto'),
    path('deletar_venda/<int:pk>', deletar_venda, name='Deletar Venda'),
]
#PARA QUE POSSA ALTERAR ALGUM OBJETO, É NECESSÁRIO QUE PASSE UMA REFERÊNCIA PARA O MESMO
#ENTÃO, CRIAMOS UMA 'PRIMARY_KEY' PARA QUE O OBJETO POSSA SER ENCONTRADO MAIS FACILMENTE