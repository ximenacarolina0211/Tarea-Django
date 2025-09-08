from django.shortcuts import render
from .models import Producto, Venta, Cliente, Proveedor

def index(request):
    ventas_producto = Producto.objects.all()
    return render(request, "ventas/index.html", {"ventas_producto": ventas_producto})

def ver_ventas(request):
    ventas = Venta.objects.all()
    return render(request, "ventas/ventas.html", {"ventas_ventas": ventas})

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "ventas/clientes.html", {"ventas_clientes": clientes})

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "ventas/proveedores.html", {"ventas_proveedores": proveedores})

def detalle_venta(request, pk):
    venta = Venta.objects.get(pk=pk)
    return render(request, "ventas/detalle_venta.html", {"venta": venta})
