# Generated by Django 2.2.2 on 2019-06-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_auto_20190618_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendas',
            name='quantidade_venda',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='vendas',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]