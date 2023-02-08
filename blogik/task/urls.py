from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog.as_view(), name='index'),
    path('task/<int:task_id>', views.ShowTask.as_view(), name='task'),
    path('add_task/', views.add_task, name='add_task'),
]
