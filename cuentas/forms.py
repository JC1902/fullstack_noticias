from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class FormularioCreacionUsuario( UserCreationForm ):
    class Meta( UserCreationForm ):
        model = Usuario
        fields = ('username', 'email', 'edad', )

class FormularioCambioUsuario( UserChangeForm ):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'edad', )