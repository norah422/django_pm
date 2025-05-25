from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from . import models
from . import forms


class Project_list_view(ListView):
    model = models.Project
    template_name = 'project/list.html'

class Project_creat_view(CreateView):
    model = models.Project
    form_class = forms.Porject_Create_Form
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')