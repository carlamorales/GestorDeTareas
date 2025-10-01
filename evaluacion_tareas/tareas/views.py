from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea

class TareaLista(ListView):
    model = Tarea

class TareaDetalle(DetailView):
    model = Tarea

class TareaCrear(CreateView):
    model = Tarea
    fields = ["titulo", "descripcion", "prioridad", "vigente", "fecha_limite"]
    success_url = reverse_lazy("tareas:tarea_list")

class TareaEditar(UpdateView):
    model = Tarea
    fields = ["titulo", "descripcion", "prioridad", "vigente", "fecha_limite"]
    success_url = reverse_lazy("tareas:tarea_list")

class TareaEliminar(DeleteView):
    model = Tarea
    success_url = reverse_lazy("tareas:tarea_list")
