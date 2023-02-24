from django.urls import path

from . import views
from .views import UserAPIView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_user, name='logout_user'),
    path('api/v2/userlist/', UserAPIView.as_view()),
]
