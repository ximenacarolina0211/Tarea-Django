from django.urls import path
from . import views

app_name = "ventas"

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.ver_ventas, name='ver_ventas'),
]
