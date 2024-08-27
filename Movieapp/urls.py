"""
URL configuration for Movieapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from movie import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/create/', views.create_movie, name='create_movie'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/create/', views.create_genre, name='create_genre'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/create/', views.create_actor, name='create_actor'),
    path('directors/', views.director_list, name='director_list'),
    path('directors/create/', views.create_director, name='create_director'),
]


