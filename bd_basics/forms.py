from django import forms
from .models import Clientes
from .models import Pedidos
from .models import Productos

class Cliente_form(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('codigo_cliente','empresa','nom_cliente','ape_cliente','puesto','direccion',
        'poblacion','telefono','cp','numero_cc')
        labels = {
            'nom_cliente':'Nombre del Cliente',
            'ape_cliente':'Apellido del Cliente',
            'cp':'Codigo Postal',
        }

class Pedido_form(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['codigo_pedido','numero_pedido','codigo_cliente','codigo_producto']

class Producto_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['codigo_producto','nombre_producto','descripcion_producto','codigo_proveedor',
        'precio_unidad','unidad_existente']


