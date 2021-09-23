from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('home/', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('feedback/', views.feedback, name='feedback'),
    path('projects/<slug:category_slug>/<slug:project_slug>', views.project_detail, name='project_detail'),
    ]