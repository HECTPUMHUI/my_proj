from django.urls import path
from . import views
from .views import TaskAPIList, TaskAPIUpdate, TaskAPIDetailView

urlpatterns = [
    # path('', views.index, name='index'),
    # path('task/<int:task_id>', views.ShowTask.as_view(), name='task'),
    # path('add_task/', views.add_task, name='add_task'),
    # path('category/<int:cat_id>/', views.show_category, name='category'),
    path('api/v1/tasklist/', TaskAPIList.as_view()),
    path('api/v1/tasklist/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/taskdetail/<int:pk>/', TaskAPIDetailView.as_view()),
]
