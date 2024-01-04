from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
]