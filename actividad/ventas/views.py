from django.shortcuts import render
from .models import Producto, Venta

def index(request):
    productos = Producto.objects.all()
    return render(request, "ventas/index.html", {"productos": productos})

def ver_ventas(request):
    ventas = Venta.objects.all()
    return render(request, "ventas/ventas.html", {"ventas": ventas})
