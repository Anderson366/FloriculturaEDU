# Generated by Django 2.2.2 on 2019-06-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20190616_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='data_admissao',
            field=models.DateTimeField(),
        ),
    ]
