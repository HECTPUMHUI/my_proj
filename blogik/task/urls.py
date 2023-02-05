from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:task_id>', views.show_task, name='task'),
    path('about/', views.about, name='about'),
]
