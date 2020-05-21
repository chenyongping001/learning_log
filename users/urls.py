"""定义learning_logs的URL模式"""
# from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name = 'users'
# 定义命名空间

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]