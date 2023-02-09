from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddTaskForm
from .models import Task


class Blog(ListView):
    model = Task
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    extra_context = {'title': 'Task List'}

    def get_queryset(self):
        return Task.objects.filter(completed=True)


class ShowTask(DetailView):
    model = Task
    template_name = 'task/task.html'
    pk_url_kwarg = 'task_id'
    context_object_name = 'task'


def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            try:
                Task.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, '!! Add  task error !!')

    else:
        form = AddTaskForm()
    return render(request, 'task/add_task.html', {'form': form, 'title': 'Add Task'})
