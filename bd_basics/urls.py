from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.menu_inicial, name='menu'),
    path('menu/pedido/', views.form_pedidos, name="insert_pedidos"),
    path('eliminar/<int:id>/', views.borrar_pedidos, name= 'delete_registros'),
    path('<int:id>/', views.form_pedidos, name= 'update_registros'),
    path('listar_pedidos/',views.listar_pedidos, name='lista_pedidos'),

    path('menu/clientes/', views.form_clientes, name="insert_clientes"),
    path('eliminar/<int:id>/', views.borrar_clientes, name= 'delete_clientes'),
    path('<int:id>/', views.form_clientes, name= 'update_clientes'),
    path('listar_clientes/',views.listar_clientes, name='lista_clientes'),

    path('menu/productos/', views.form_productos, name="insert_productos"),
    path('eliminar/<int:id>/', views.borrar_productos, name= 'delete_productos'),
    path('<int:id>/', views.form_productos, name= 'update_productos'),
    path('listar_productos/',views.listar_productos, name='lista_productos'),

]