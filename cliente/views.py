from django.shortcuts import render, redirect
from .form import ClientesForm
#from .form import FuncionariosForm
#from .form import ProdutosForm
#from .form import VendasForm

# Create your views here.

import datetime
from .models import Clientes
from .models import Funcionarios
from .models import Produtos
from .models import Vendas

def home(request):
    now = datetime.datetime.now()
    #html = "<html><body>São exatamente: %s </body></html>" % now
    return render(request, 'cliente/home.html')

#render retorna a página html passada como parâmetro e uma request
def lista(request):
    data = {}
    #DICIONÁRIO DATA
    data ['cliente'] = Clientes.objects.all()
    return render(request, 'cliente/lista_cliente.html', data)

def cadastrar_cliente(request):
    form = ClientesForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'cliente/cadastrar_cliente.html', {'form': form})

def atualizar_cliente(request, pk):
    data = {}
    cliente = Clientes.objects.get(pk=pk)
    form = ClientesForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista')
    data['form'] = form
    data['cliente'] = cliente
    return render(request, 'cliente/cadastrar_cliente.html', data)

    #ESTA FUNÇÃO FOI CRIADA PARA QUE POSSAMOS EDITAR DADOS JÁ SALVOS NO NOSSO BANCO DE DADOS
    #UTILIZANDO A CHAVE PRIMÁRIA DA CLASSE E PASSANDO UM FORMULÁRIO JÁ PREENCHIDO COM OS MESMOS DADOS DO OBJETO
    #O OBJETO SERÁ ENCONTRADO NO BANCO DE DADOS COM O USO DO MÉTODO 'GET' E O FORMULÁRIO 'OR NONE' (NÃO VAZIO)

def deletar_cliente(request, pk):
    cliente = Clientes.objects.get(pk=pk)
    cliente.delete()
    return redirect('lista')
