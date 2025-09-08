from django.urls import path
from . import views

app_name = "ventas"

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.ver_ventas, name='ver_ventas'),
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('detalle/<str:pk>/', views.detalle_venta, name='detalle_venta'),
]
