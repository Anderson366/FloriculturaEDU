from django.shortcuts import render, redirect
from .form import ClientesForm
from .form import FuncionariosForm
from .form import ProdutosForm
from .form import VendasForm
from .form import ErrosForm


from .models import Clientes
from .models import Funcionarios
from .models import Produtos
from .models import Vendas
from .models import Erros

def base(request):
    return render(request, 'cliente/base.html')

def sobre(request):
    return render(request, 'cliente/sobre.html')

def home(request):
    #now = datetime.datetime.now()
    #html = "<html><body>São exatamente: %s </body></html>" % now
    return render(request, 'cliente/home.html')

#render retorna a página html passada como parâmetro e uma request

def lista_cliente(request):
    data = {}
    #DICIONÁRIO DATA
    data ['cliente'] = Clientes.objects.all()
    return render(request, 'cliente/lista_cliente.html', data)
def cadastrar_cliente(request):
    form = ClientesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Lista Cliente')
    return render(request, 'cliente/cadastrar_cliente.html', {'form': form})
def atualizar_cliente(request, pk):
    data = {}
    cliente = Clientes.objects.get(pk=pk)
    form = ClientesForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('Lista Cliente')
    data['form'] = form
    data['cliente'] = cliente
    return render(request, 'cliente/cadastrar_cliente.html', data)
    #ESTA FUNÇÃO FOI CRIADA PARA QUE POSSAMOS EDITAR DADOS JÁ SALVOS NO NOSSO BANCO DE DADOS
    #UTILIZANDO A CHAVE PRIMÁRIA DA CLASSE E PASSANDO UM FORMULÁRIO JÁ PREENCHIDO COM OS MESMOS DADOS DO OBJETO
    #O OBJETO SERÁ ENCONTRADO NO BANCO DE DADOS COM O USO DO MÉTODO 'GET' E O FORMULÁRIO 'OR NONE' (NÃO VAZIO)
def deletar_cliente(request, pk):
    cliente = Clientes.objects.get(pk=pk)
    cliente.delete()
    return redirect('Lista Cliente')


def lista_funcionario(request):
    data = {}
    data ['funcionario'] = Funcionarios.objects.all()
    return render(request, 'cliente/lista_funcionario.html', data)
def cadastrar_funcionario(request):
    form = FuncionariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Lista Funcionario')
    return render(request, 'cliente/cadastrar_funcionario.html', {'form': form})
def atualizar_funcionario(request, pk):
    data = {}
    funcionario = Funcionarios.objects.get(pk=pk)
    form = FuncionariosForm(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('Lista Funcionario')
    data['form'] = form
    data['funcionario'] = funcionario
    return render(request, 'cliente/cadastrar_funcionario.html', data)
def deletar_funcionario(request, pk):
    funcionario = Funcionarios.objects.get(pk=pk)
    funcionario.delete()
    return redirect('Lista Funcionario')


def lista_produto(request):
    data = {}
    data ['produto'] = Produtos.objects.all()
    return render(request, 'cliente/lista_produto.html', data)
def cadastrar_produto(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Lista Produto')
    return render(request, 'cliente/cadastrar_produto.html', {'form': form})
def atualizar_produto(request, pk):
    data = {}
    produto = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('Lista Produto')
    data['form'] = form
    data['produto'] = produto
    return render(request, 'cliente/cadastrar_produto.html', data)
def deletar_produto(request, pk):
    produto = Produtos.objects.get(pk=pk)
    produto.delete()
    return redirect('Lista Produto')


def lista_venda(request):
    data = {}
    data['venda'] = Vendas.objects.all()
    return render(request, 'cliente/lista_venda.html', data)
def cadastrar_venda(request):
    form = VendasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Lista Venda')
    return render(request, 'cliente/cadastrar_venda.html', {'form': form})
def atualizar_venda(request, pk):
    data = {}
    venda = Vendas.objects.get(pk=pk)
    form = VendasForm(request.POST or None, instance=venda)
    if form.is_valid():
        form.save()
        return redirect('Lista Venda')
    data['form'] = form
    data['venda'] = venda
    return render(request, 'cliente/cadastrar_venda.html', data)
def deletar_venda(request, pk):
    venda = Vendas.objects.get(pk=pk)
    venda.delete()
    return redirect('Lista Venda')

def lista_erro(request):
    data = {}
    data ['erro'] = Erros.objects.all()
    return render(request, 'cliente/lista_erro.html', data)
def cadastrar_erro(request):
    form = ErrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Lista Erro')
    return render(request, 'cliente/relatar_erro.html', {'form': form})
def atualizar_erro(request, pk):
    data = {}
    erro = Erros.objects.get(pk=pk)
    form = ErrosForm(request.POST or None, instance=erro)
    if form.is_valid():
        form.save()
        return redirect('Lista Erro')
    data['form'] = form
    data['erro'] = erro
    return render(request, 'cliente/relatar_erro.html', data)
def deletar_erro(request, pk):
    erro = Erros.objects.get(pk=pk)
    erro.delete()
    return redirect('Lista Erro')
