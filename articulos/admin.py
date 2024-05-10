from django.contrib import admin
from .models import Articulo, Comentarios

class ComentariosEnLinea(admin.TabularInline):
    model = Comentarios
    extra = 1

class ArticuloAdmin(admin.ModelAdmin):
    inlines = [
        ComentariosEnLinea,
    ]

# Register your models here.
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentarios)

