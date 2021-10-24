from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import *

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'app1/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(completed= False)
        return context


class AddTask(CreateView):
    model = Task
    fields= ['title', 'description', 'due_date', 'priority', 'task_type']
    template_name = 'app1/managetask.html'

class AddTaskType(CreateView):
    model = TaskType
    fields= ['description', 'name']
    template_name = 'app1/managetask.html'