from django.contrib import admin

# Register your models here.
#rama master añadiendo esta linea
from .models import provedor,pedido,producto,Cliente



admin.site.register(provedor)
admin.site.register(pedido)
admin.site.register(producto)
admin.site.register(Cliente)

