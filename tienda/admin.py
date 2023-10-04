from django.contrib import admin
from .models import Categoria, Producto, Cliente

# Definimos una acción personalizada para actualizar el stock a cero
def actuStockCero(modeladmin, request, queryset):
    queryset.update(stock=0)

# Configuramos la descripción corta para la acción
actuStockCero.short_description = "Actualizar stock a cero"

# Registramos el modelo Categoria en el administrador
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pub_date')

admin.site.register(Categoria, CategoriaAdmin)

# Registramos el modelo Producto en el administrador
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'pub_date')
    actions = [actuStockCero] 

admin.site.register(Producto, ProductoAdmin)

# Registramos el modelo Cliente en el administrador
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nac', 'fecha_pub')

admin.site.register(Cliente, ClienteAdmin)