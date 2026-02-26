
# Proyecto Django: Distribuidora de Alimentos
# Alumno: Szakura Lautaro

Nota: Al proyecto le falta, la parte CSS, no lo inclui debido a que no termine de entender esa parte y quise entregar lo que tenia hasta el momento


#Descripcion

Este proyecto es una web de gestión para una distribuidora de alimentos.  
Permite crear **proveedores**, **locales**, **productos** y buscar productos por nombre.
El proyecto está desarrollado en **Django**, usando el patrón **MVT** y herencia de plantillas HTML.


#Funcionalidades

*Crear Proveedores: Permite ingresar nombre, teléfono y correo electrónico.
*Crear Locales: Permite ingresar nombre, dirección y ciudad.
*Crear Productos: Permite ingresar nombre, precio, stock y asociarlo a un proveedor y un local.
*Buscar Productos: Permite buscar productos por nombre (búsqueda parcial incluida).

Proyecto/
├─ gestion/             
│  ├─ templates/
│  │  └─ gestion/
│  │     ├─ base.html
│  │     ├─ inicio.html
│  │     ├─ crear_proveedor.html
│  │     ├─ crear_local.html
│  │     ├─ crear_producto.html
│  │     ├─ buscar_producto.html
│  │     └─ resultados.html
│  ├─ models.py
│  ├─ views.py
│  ├─ forms.py
│  ├─ urls.py
│  └─ admin.py
├─ distribuidora/
│  ├─ settings.py
│  └─ urls.py
├─ manage.py
└─ .gitignore
