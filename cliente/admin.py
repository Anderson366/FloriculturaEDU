from django.contrib import admin

# Register your models here.
from .models import Clientes
from .models import Funcionarios
from .models import Produtos
from .models import Vendas
from .models import Erros

class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'nome_produto',
class VendaAdmin(admin.ModelAdmin):
    list_display = 'nome_venda',

admin.site.register(Clientes)
admin.site.register(Funcionarios)
admin.site.register(Produtos)
admin.site.register(Vendas)
admin.site.register(Erros)

admin.site.site_header = 'MiniDevs'
admin.site.index_title = 'Floricultura'
admin.site.site_title = 'ADM - Floricultura'