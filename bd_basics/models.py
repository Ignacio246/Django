from django.db import models

# Create your models here.

class Clientes(models.Model):
    codigo_cliente = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    nom_cliente = models.CharField(max_length=50)
    ape_cliente = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    cp = models.CharField(max_length=50)
    numero_cc = models.CharField(max_length=50)
    


class Pedidos(models.Model):
    codigo_pedido = models.CharField(max_length=50)
    numero_pedido = models.CharField(max_length=50)
    codigo_producto = models.CharField(max_length=50)
    codigo_cliente = models.CharField(max_length=50)

class Productos(models.Model):
    codigo_producto = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=50)
    descripcion_producto = models.CharField(max_length=50)
    codigo_proveedor = models.CharField(max_length=50)
    precio_unidad = models.CharField(max_length=50)
    unidad_existente = models.CharField(max_length=50)
