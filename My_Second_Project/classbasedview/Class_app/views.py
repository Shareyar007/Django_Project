from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from Class_app.models import Person
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class IndexView(ListView):
    context_object_name = 'person_list'
    model = Person
    template_name = 'Class_app/index.html'

class MoreInfo(DetailView):
    context_object_name = 'person'
    model = Person
    template_name = 'Class_app/detailview.html'

class AddPerson(CreateView):
    model = Person
    fields = ('name', 'email', 'shirt_size')
    template_name = 'Class_app/person_form.html'

class UpdatePerson(UpdateView):
    model = Person
    fields = ('shirt_size',)
    template_name = 'Class_app/person_form.html'

class DeletePerson(DeleteView):
    context_object_name = 'person'
    model = Person
    success_url = reverse_lazy("class_app:viewindexcd")
    template_name = 'Class_app/delete_person.html'

