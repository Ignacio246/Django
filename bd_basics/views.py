from django.shortcuts import redirect, render
from .models import Pedidos
from .models import Clientes
from .models import Productos
from .forms import Cliente_form
from .forms import Pedido_form
from .forms import Producto_form
# Create your views here.

def menu_inicial(request):
    return render(request, "C:/app/app1/bd_basics/templates/registros/menu.html")



def form_clientes(request, id=0):
    if request.method == "GET":
        if id ==0:
            form = Cliente_form()
        else:
            Cliente = Clientes.objects.get(pk=id)
            form = Cliente_form(instance=Cliente)
        
        return render(request, 'registros/form_clientes.html',{'form':form})
    else:
        if id==0:
            form = Cliente_form(request.POST)
        else:
             Cliente = Clientes.objects.get(pk=id)
             form = Cliente_form(request.POST, instance=Cliente)
        if(form.is_valid()):
            form.save()
        return redirect('/clientes/listar_clientes')
        
def listar_clientes(request):

    context = {'listar_clientes' : Clientes.objects.all()}
    return render(request, 'registros/listar_clientes.html',context)

def borrar_clientes(request,id):
    Cliente = Clientes.objects.get(pk=id)
    Cliente.delete()
    return redirect('/clientes/listar_clientes')

    
def form_pedidos(request, id=0):
    if request.method == "GET":
        if id ==0:
            form = Pedido_form()
        else:
            Pedido = Pedidos.objects.get(pk=id)
            form = Pedido_form(instance=Pedido)
        
        return render(request, 'registros/form_pedidos.html',{'form':form})
    else:
        if id==0:
            form = Pedido_form(request.POST)
        else:
             Pedido = Pedidos.objects.get(pk=id)
             form = Pedido_form(request.POST, instance=Pedido)
        if(form.is_valid()):
            form.save()
        return redirect('/pedido/listar_pedidos')

def listar_pedidos(request):

    context = {'listar_pedidos' : Pedidos.objects.all()}
    return render(request, 'registros/listar_pedidos.html',context)

def borrar_pedidos(request,id):
    Pedido = Pedidos.objects.get(pk=id)
    Pedido.delete()
    return redirect('/pedido/listar_pedidos')


def form_productos(request, id=0):
    if request.method == "GET":
        if id ==0:
            form = Producto_form()
        else:
            Producto = Productos.objects.get(pk=id)
            form = Producto_form(instance=Producto)
        
        return render(request, 'registros/form_productos.html',{'form':form})
    else:
        if id==0:
            form = Producto_form(request.POST)
        else:
             Producto = Productos.objects.get(pk=id)
             form = Producto_form(request.POST, instance=Producto)
        if(form.is_valid()):
            form.save()
        return redirect('/productos/listar_productos')

def listar_productos(request):

    context = {'listar_productos' : Productos.objects.all()}
    return render(request, 'registros/listar_productos.html',context)

def borrar_productos(request,id):
    Producto = Productos.objects.get(pk=id)
    Producto.delete()
    return redirect('/productos/listar_productos')



