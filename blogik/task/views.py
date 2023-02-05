from django.http import HttpResponse
from django.shortcuts import render

tasks = ['Go to street walk', 'Go to work', 'By present']


# Create your views here.
def index(request):
    return render(request, 'task/index.html', {'tasks': tasks, 'title': 'Task Page'})


def about(request):
    return render(request, 'task/about.html', {'title': 'About'})
