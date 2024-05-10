from django import forms
from .models import Comentarios

class FormularioComentario( forms.ModelForm ):
    class Meta:
        model = Comentarios
        fields = ( 'comentario', 'autor' )