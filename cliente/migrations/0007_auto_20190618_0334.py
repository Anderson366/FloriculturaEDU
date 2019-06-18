# Generated by Django 2.2.2 on 2019-06-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_auto_20190617_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendas',
            name='quantidade',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='vendas',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default='', max_digits=6),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='rg_cliente',
            field=models.CharField(default='00000000', max_length=7),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefone_cliente',
            field=models.CharField(default='00000000', max_length=11),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='rg_funcionario',
            field=models.CharField(default='0000000', max_length=7),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='telefone_funcionario',
            field=models.CharField(default='00000000000', max_length=11),
        ),
    ]