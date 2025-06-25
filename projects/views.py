from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms


class Project_list_view(ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 6

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class Project_creat_view(CreateView):
    model = models.Project
    form_class = forms.Porject_Create_Form
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')


class Project_update_view(UpdateView):
    model = models.Project
    form_class = forms.Porject_Update_Form
    template_name = 'project/update.html'

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id])


class Project_delete_view(DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_list')


class Task_creat_view(CreateView):
    model = models.Task
    fields = ['project', 'description']
    template_name = 'project/create.html'
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class Task_update_view(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class Task_delete_view(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])