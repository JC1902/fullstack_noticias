from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from .models import Articulo
from .forms import FormularioComentario

class ComentarioGet( DetailView ):
    model = Articulo
    template_name = 'detalle_articulo.html'

    def get_context_data( self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context['form'] = FormularioComentario()

        return context
    
class ComentarioPost( SingleObjectMixin, FormView ):
    model = Articulo
    form_class = FormularioComentario
    template_name = 'detalle_articulo.html'

    def pos(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comentario = form.save(commit=False)
        comentario.articulo = self.object
        comentario.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        articulo = self.get_object()
        return reverse('detalle_artculo', kwargs={'pk': articulo.pk})

# Create your views here.
class VistaListaArticulos( LoginRequiredMixin, ListView ):
    model = Articulo
    template_name = 'lista_articulos.html'

class VistaDetalleArticulo( LoginRequiredMixin , DetailView ):
    def get(self, request, *args, **kwargs):
        vista = ComentarioGet.as_view()
        return vista(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        vista = ComentarioPost.as_view()
        return vista(request, *args, **kwargs)
    # model = Articulo
    # template_name = 'detalle_articulo.html'

    # def get_context_data( self, **kwargs ):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = FormularioComentario()

    #     return context

class VistaEditarArticulo( LoginRequiredMixin, UpdateView ):
    model = Articulo
    fields = (
        'titulo',
        'cuerpo',
    )
    template_name = 'editar_articulo.html'

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

class VistaEliminarArticulo( LoginRequiredMixin, DeleteView ):
    model = Articulo
    template_name = 'eliminar_articulo.html'
    success_url = reverse_lazy('lista_articulos')

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

class VistaNuevoArticulo( LoginRequiredMixin, CreateView ):
    model = Articulo
    template_name = 'nuevo_articulo.html'
    fields = (
        'titulo',
        'cuerpo',
    )

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)