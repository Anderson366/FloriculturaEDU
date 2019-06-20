from django.forms import ModelForm
from .models import Clientes
from .models import Funcionarios
from .models import Produtos
from .models import Vendas
from .models import Erros

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
        fields = ['nome_produto', 'quantidade_produto', 'valor_produto', 'descricao', 'observacao']

class VendasForm(ModelForm):
    class Meta:
        model = Vendas
        fields = ['nome_venda', 'cliente', 'produto', 'funcionario', 'quantidade_venda', 'valor_total']

class ErrosForm(ModelForm):
    class Meta:
        model = Erros
        fields = ['nome_relato', 'descricao_erro']

#SEMPRE COLOCAR OS MESMOS NOMES CONTIDOS NAS CLASSES DENTRO DE MODELS.PY