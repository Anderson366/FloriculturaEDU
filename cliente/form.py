from django.forms import ModelForm
from .models import Clientes
from .models import Funcionarios
from .models import Produtos
from .models import Vendas

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome_cliente','rg_cliente', 'endereco_cliente', 'telefone_cliente']

class FuncionariosForm(ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome_funcionario', 'rg_funcionario', 'endereco_funcionario', 'telefone_funcionario', 'data_admissao', 'salario']

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome_produto', 'descricao', 'quantidade', 'valor', 'observacao']

class VendasForm(ModelForm):
    class Meta:
        model = Vendas
        fields = ['nome_venda', 'cliente', 'produto', 'funcionario', 'quantidade', 'valor_total']

#SEMPRE COLOCAR OS MESMOS NOMES CONTIDOS NAS CLASSES DENTRO DE MODELS.PY