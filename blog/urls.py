from django.urls import path
from . import views
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<str:username>/', views.perfil, name='perfil'),
    path('seguir/<str:username>/', views.seguir, name='seguir'),
    path('dejarseguir/<str:username>/', views.dejarseguir, name='dejarseguir'),
    path('wiki/', views.wiki, name='wiki'),
    path('wiki/mecanicas/', views.mecanicas, name='mecanicas'),
]
