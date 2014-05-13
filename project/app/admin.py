# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import *

class ProveedAdmin(admin.ModelAdmin):
    filter_horizontal = ['productos']

    list_filter = ('productos',)
class RecetAdmin(admin.ModelAdmin):
    filter_horizontal = ['clavemateriaprima']

class ProducAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Nombre del producto', {
            'fields': ('nombre','descripcion')
        }),
        ('Descripcion del producto', {
            'classes': ('collapse',),
            'description': 'Captura los datos del producto',
            'fields': ('precio', 'cantidad', 'categoria')
        }),
	)
    list_display = ('nombre', 'id', 'precio')

    list_editable = ('precio',)

    list_filter = ('categoria',)

    search_fields = ('nombre',)
   
admin.site.register(Categoria)
admin.site.register(Producto, ProducAdmin)
admin.site.register(UnidadPresentacion)
admin.site.register(Proveedore, ProveedAdmin)
admin.site.register(MateriaPrima)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(VentasProducto)
admin.site.register(Receta, RecetAdmin)



# Register your models here.
