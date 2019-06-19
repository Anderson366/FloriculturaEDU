from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=100, default='')
    rg_cliente = models.CharField(max_length=7, default='0000000')
    endereco_cliente = models.CharField(max_length=50, default='')
    telefone_cliente = models.CharField(max_length=11, default='00000000')

    def __str__(self):
        return self.nome_cliente
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Funcionarios(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=100, default='')
    rg_funcionario = models.CharField(max_length=7, default='0000000')
    endereco_funcionario = models.CharField(max_length=50, default='')
    telefone_funcionario = models.CharField(max_length=11, default='00000000000')
    data_admissao = models.DateTimeField(auto_now_add=False)
    salario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome_funcionario
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=100, default='')
    quantidade_produto = models.IntegerField()
    valor_produto = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    observacao = models.TextField(null = True, blank = True, default='-')

    def __str__(self):
        return self.nome_produto
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

class Vendas(models.Model):
    id_venda = models.AutoField(primary_key=True)
    nome_venda = models.CharField(max_length=100, default='')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    quantidade_venda = models.IntegerField(max_length=5, default=0)
#    quantidade_venda = models.IntegerField(default=10)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    data_venda = models.DateTimeField(auto_now_add=True)

    #FALTOU COLOCAR A QUANTIDADE DO ESTOQUE
    #FALTOU COLOCAR O VALOR DA VENDA

    def __str__(self):
        return self.nome_venda
    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

class Erros(models.Model):
    id_erro = models.AutoField(primary_key=True)
    nome_relato = models.CharField(max_length=50)
    descricao_erro = models.TextField()

    def __str__(self):
        return self.nome_relato
    class Meta:
        verbose_name = 'Erro'
        verbose_name_plural = 'Erros'


#FALTANDO INTERAGIR COM O BANCO DE DADOS PARA QUE A VENDA POSSA SER EFETUADA DE FORMA ESTÁTICA

#VOU ANOTAR ISSO PARA QUE EU NÃO ESQUEÇA
#CRIAR UM JAVASCRIPT PARA QUE, AO CONCLUIR A VENDA OU INSERIR UM PRODUTO, APAREÇA UMA MENSAGEM EM POP-UP NA TELA
#COM A MENSAGEM POSITIVA, OU DE ALGUM POSSÍVEL ERRO E QUE ESTA PÁGINA, AO CLICAR EM 'OK', SEJA REDIRECIONADA PARA ALGUMA OUTRA LISTAGEM.