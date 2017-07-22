from django.contrib import admin
from .models import Categoria, Proveedor, Producto, Cliente, Factura, DetalleFactura

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Cliente)

class detalle_FacturaInLine(admin.TabularInline):
	model = DetalleFactura

class facturaAdmin(admin.ModelAdmin):
	inlines = (detalle_FacturaInLine,)

admin.site.register(Factura, facturaAdmin)
