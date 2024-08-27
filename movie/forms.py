from .models import Movie, Genre, Actor, Director
from django import forms
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'release_date', 'runtime', 'plot', 'poster', 'genres', 'actors', 'directors')

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name', 'description')

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ('first_name', 'last_name', 'date_of_birth', 'bio')

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ('first_name', 'last_name', 'date_of_birth', 'bio')


