# Generated by Django 2.2.2 on 2019-06-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_auto_20190618_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='quantidade',
            field=models.IntegerField(default=10),
        ),
    ]