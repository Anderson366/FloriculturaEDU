# Generated by Django 2.2.2 on 2019-06-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0010_auto_20190618_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='rg_cliente',
            field=models.CharField(default='0000000', max_length=7),
        ),
    ]
