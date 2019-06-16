from django.forms import ModelForm
from .models import Clientes
from .models import Funcionarios
from .models import Produtos
from .models import Vendas

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome_cliente','rg_cliente', 'endereco_cliente', 'telefone_cliente']

#SEMPRE COLOCAR OS MESMOS NOMES CONTIDOS NAS CLASSES DENTRO DE MODELS.PY