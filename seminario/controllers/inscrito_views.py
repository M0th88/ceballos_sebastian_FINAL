from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Inscrito
from ..forms import InscritoForm

# Listar Inscritos
class InscritoListView(ListView):
    model = Inscrito
    template_name = 'inscrito_list.html'
    context_object_name = 'inscritos'

# Crear un Inscrito
class InscritoCreateView(CreateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = 'inscrito_form.html'
    success_url = reverse_lazy('inscrito_list')

# Editar un Inscrito
class InscritoUpdateView(UpdateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = 'inscrito_form.html'
    success_url = reverse_lazy('inscrito_list')

# Eliminar un Inscrito
class InscritoDeleteView(DeleteView):
    model = Inscrito
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('inscrito_list')


