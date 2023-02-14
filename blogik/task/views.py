from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView, CreateView

from .forms import AddTaskForm
from .models import Task, Category


# class Blog(ListView):
#     model = Task
#     template_name = 'task/index.html'
#     context_object_name = 'tasks'
#     extra_context = {'title': 'Task List'}
#
#     def get_queryset(self):
#         return Task.objects.filter(completed=True)
def index(request):
    tasks = Task.objects.all()
    cats = Category.objects.all()

    context = {
        'tasks': tasks,
        'cats': cats,
        'title': 'Task List',
        'cat_selected': 0,
    }

    return render(request, 'task/index.html', context=context)


class ShowTask(DetailView):
    model = Task
    template_name = 'task/task.html'
    pk_url_kwarg = 'task_id'
    context_object_name = 'task'
    extra_context = {'title': 'Task'}


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


def show_category(request, cat_id):
    tasks = Task.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(tasks) == 0:
        raise Http404()

    context = {
        'tasks': tasks,
        'cats': cats,
        'title': 'Category view',
        'cat_selected': cat_id,
    }

    return render(request, 'task/index.html', context=context)
