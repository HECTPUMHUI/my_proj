from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import datetime

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


# def index(request):
#     tasks = Task.objects.all()
#     return render(request, 'task/index.html', {'tasks': tasks, 'title': 'Tasks'})

class ShowTask(DetailView):
    model = Task
    template_name = 'task/task.html'
    pk_url_kwarg = 'task_id'
    context_object_name = 'task'


# class AddTask(CreateView):
#     form_class =
#     template_name = 'task/add_task.html'

def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Task.objects.create(**form.cleaned_data)
                return redirect('index')
            except:
                form.add_error(None, '!! Add  task error !!')

    else:
        form = AddTaskForm()
    return render(request, 'task/add_task.html', {'form': form, 'title': 'Add Task'})
# def show_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)
#
#     context = {
#         'task': task,
#         'time': datetime.datetime.now(),
#     }
#
#     return render(request, 'task/task.html', context=context)
