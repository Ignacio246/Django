# Generated by Django 3.2.4 on 2021-06-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_basics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='codigo_cliente',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='productos',
            name='codigo_producto',
            field=models.CharField(max_length=50),
        ),
    ]
