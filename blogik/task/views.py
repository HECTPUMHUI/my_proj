from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime

from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'task/index.html', {'tasks': tasks, 'title': 'Tasks'})


def show_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    context = {
        'task': task,
        'time': datetime.datetime.now(),
    }

    return render(request, 'task/task.html', context=context)


def about(request):
    return render(request, 'task/about.html', {'title': 'About'})
