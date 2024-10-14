from django.contrib import admin

from .models import Categoria, Proveedor, Cliente, Farmacia, Empleado, Inventario, Medicamento, Receta, Pedido, Venta

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Farmacia)
admin.site.register(Empleado)
admin.site.register(Inventario)
admin.site.register(Medicamento)
admin.site.register(Receta)
admin.site.register(Pedido)
admin.site.register(Categoria)
admin.site.register(Venta)