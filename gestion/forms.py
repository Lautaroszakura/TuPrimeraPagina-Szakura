from django import forms
from .models import Proveedor, Local, Producto

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields='__all__'
    
class LocalForm(forms.ModelForm):
    class Meta:
        model=Local
        fields='__all__'

class ProductoForm(forms.ModelForm):
    class meta:
        model=Producto
        fields='__all__'
        
class BuscarProductoForm(forms.Form):
    nombre=forms.CharField(max_length=40)
