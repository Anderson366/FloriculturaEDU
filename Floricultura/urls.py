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
from cliente.views import base
from cliente.views import sobre

from cliente.views import lista_cliente
from cliente.views import lista_funcionario
from cliente.views import lista_produto
from cliente.views import lista_venda
from cliente.views import lista_erro

from cliente.views import cadastrar_cliente
from cliente.views import cadastrar_funcionario
from cliente.views import cadastrar_produto
from cliente.views import cadastrar_venda
from cliente.views import cadastrar_erro

from cliente.views import atualizar_cliente
from cliente.views import atualizar_funcionario
from cliente.views import atualizar_produto
from cliente.views import atualizar_venda
from cliente.views import atualizar_erro

from cliente.views import deletar_cliente
from cliente.views import deletar_funcionario
from cliente.views import deletar_produto
from cliente.views import deletar_venda
from cliente.views import deletar_erro


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='Home'),
    path('sobre/', sobre, name='Sobre'),
    path('', base, name='Base'),


    path('lista_cliente/', lista_cliente, name='Lista Cliente'),
    path('lista_funcionario/', lista_funcionario, name='Lista Funcionario'),
    path('lista_produto/', lista_produto, name='Lista Produto'),
    path('lista_venda/', lista_venda, name='Lista Venda'),
    path('lista_erro/', lista_erro, name='Lista Erro'),


    path('cadastrar_cliente/', cadastrar_cliente, name='Cadastro Cliente'),
    path('cadastrar_funcionario/', cadastrar_funcionario, name='Cadastro Funcionario'),
    path('cadastrar_produto/', cadastrar_produto, name='Cadastro Produto'),
    path('cadastrar_venda/', cadastrar_venda, name='Cadastro Venda'),
    path('relatar_erro/', cadastrar_erro, name='Cadastro Erro'),

    path('atualizar_cliente/<int:pk>', atualizar_cliente, name='Atualizar Cliente'),
    path('atualizar_funcionario/<int:pk>', atualizar_funcionario, name='Atualizar Funcionario'),
    path('atualizar_produto/<int:pk>', atualizar_produto, name='Atualizar Produto'),
    path('atualizar_venda/<int:pk>', atualizar_venda, name='Atualizar Venda'),
    path('atualizar_erro/<int:pk>', atualizar_erro, name='Atualizar Erro'),

    path('deletar_cliente/<int:pk>', deletar_cliente, name='Deletar Cliente'),
    path('deletar_funcionario/<int:pk>', deletar_funcionario, name='Deletar Funcionario'),
    path('deletar_produto/<int:pk>', deletar_produto, name='Deletar Produto'),
    path('deletar_venda/<int:pk>', deletar_venda, name='Deletar Venda'),
    path('deletar_erro/<int:pk>', deletar_erro, name='Deletar Erro'),
]
#PARA QUE POSSA ALTERAR ALGUM OBJETO, É NECESSÁRIO QUE PASSE UMA REFERÊNCIA PARA O MESMO
#ENTÃO, CRIAMOS UMA 'PRIMARY_KEY' PARA QUE O OBJETO POSSA SER ENCONTRADO MAIS FACILMENTE