from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import auth
from .forms import FormularioCreacionUsuario, FormularioCambioUsuario
from .models import Usuario

class UsuarioAdmin( UserAdmin ):
    add_form = FormularioCreacionUsuario
    form = FormularioCambioUsuario
    model = Usuario
    list_display = [
        'email',
        'username',
        'edad',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('edad',) }),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('edad' ,)}),)

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)