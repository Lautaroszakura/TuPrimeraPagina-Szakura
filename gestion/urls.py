from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('proveedor/', crear_proveedor, name="crear_proveedor"),
    path('local/', crear_local, name="crear_local"),
    path('producto/', crear_producto, name="crear_producto"),
    path('buscar/', buscar_producto, name="buscar_producto"),
]