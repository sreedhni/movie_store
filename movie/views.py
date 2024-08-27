from django.shortcuts import render, redirect
from .forms import MovieForm, GenreForm, ActorForm, DirectorForm
from .models import Movie, Genre, Actor, Director

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'create_movie.html', {'form': form})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()
    return render(request, 'create_genre.html', {'form': form})

def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'actor_list.html', {'actors': actors})

def create_actor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actor_list')
    else:
        form = ActorForm()
    return render(request, 'create_actor.html', {'form': form})

def director_list(request):
    directors = Director.objects.all()
    return render(request, 'director_list.html', {'directors': directors})

def create_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director_list')
    else:
        form = DirectorForm()
    return render(request, 'create_director.html', {'form': form})


