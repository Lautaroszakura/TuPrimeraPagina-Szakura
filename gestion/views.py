from django.shortcuts import render
from .forms import *
from .models import Producto

# Create your views here.

def inicio(request):
    return render(request, "gestion/inicio.html")

def crear_proveedor(request):
    if request.method=="POST":
        form=ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gestion/inicio.html")
    else:
        form=ProveedorForm()
    return render(request,"gestion/crear_proveedor.html",{"form":form})

def crear_local(request):
    if request.method=="POST":
        form=LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"gestion/inicio.html")
    else:
        form=ProductoForm()
    return render(request,"gestion/crear_producto.html",{"form":form})
    
def crear_producto(request):
    if request.method=="POST":
        form=ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"gestion/inicio.html")
        else:
            form=ProductoForm()
    return render(request,"gestion/crear_producto.html",{"form":form})

def buscar_producto(request):
    if request.method=="GET":
        form=BuscarProductoForm(request.GET)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            productos=productos.objects.filter(nombre_icontains=nombre)
            return render(request,"gestion/resultados.html",{"productos":productos})
    form=BuscarProductoForm()
    return render(request,"gestion/buscar_producto.html",{"form":form})
        