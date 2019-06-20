# Generated by Django 2.2.2 on 2019-06-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_vendas_quantidade_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='endereco_cliente',
            field=models.CharField(default='', max_length=50, verbose_name='Endereço do Cliente'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nome_cliente',
            field=models.CharField(default='', max_length=100, verbose_name='Nome do Cliente'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='rg_cliente',
            field=models.CharField(default='0000000', max_length=7, verbose_name='RG do Cliente'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefone_cliente',
            field=models.CharField(default='00000000', max_length=11, verbose_name='Telefone do Cliente'),
        ),
        migrations.AlterField(
            model_name='erros',
            name='descricao_erro',
            field=models.TextField(verbose_name='Descrição do Erro'),
        ),
        migrations.AlterField(
            model_name='erros',
            name='nome_relato',
            field=models.CharField(max_length=50, verbose_name='Nome do Relator'),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='data_admissao',
            field=models.DateTimeField(verbose_name='Data de Admissão'),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='endereco_funcionario',
            field=models.CharField(default='', max_length=50, verbose_name='Endereço do Funcionário'),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='nome_funcionario',
            field=models.CharField(default='', max_length=100, verbose_name='Nome do Funcionário'),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='rg_funcionario',
            field=models.CharField(default='0000000', max_length=7, verbose_name='RG do Funcionário'),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Salário'),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='telefone_funcionario',
            field=models.CharField(default='00000000000', max_length=11, verbose_name='Telefone do Funcionário'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='nome_produto',
            field=models.CharField(default='', max_length=100, verbose_name='Nome do Produto'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='observacao',
            field=models.TextField(blank=True, default='-', null=True, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='quantidade_produto',
            field=models.IntegerField(verbose_name='Quantidade em Estoque'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='valor_produto',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor Unidade'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='data_venda',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data da Venda'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='nome_venda',
            field=models.CharField(default='', max_length=100, verbose_name='Nome da Venda'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='quantidade_venda',
            field=models.IntegerField(default=0, verbose_name='Quantidade do Produto'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Valor Total da Venda'),
        ),
    ]
