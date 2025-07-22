from django.contrib import admin
from django.urls import path
from Website import views
from .views import video
from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.homepage),
    path('Movies',views.Movies),
    path('Trailers',views.Trailers),
    path('News',views.News),
    path('Songs',views.Songs),
    path('movie1',views.Movie1),
    path('movie2',views.Movie2),
    path('movie3',views.Movie3),
    path('movie4',views.Movie4),
    path('movie5',views.Movie5),
    path('movie6',views.Movie6),
    path('playlist1',views.playlist1),
    path('playlist2',views.playlist2),
    path('playlist3',views.playlist3),
    path('playlist4',views.playlist4),
    path('playlist5',views.playlist5),
    path('playlist6',views.playlist6),
    path('Stories',views.Stories),
    path('Horror',views.Horror),
    path('Thriller',views.Thriller),
    path('Mystery',views.Mystery),
    path('Science Fiction',views.Science_Fiction),
    path('Adventure',views.Adventure),
    path('Action',views.Action),
    path('Fantasy',views.Fantasy),
    path('Games',views.Games),
    path('The_Yellow_Wall_paper',views.hstory1),
    path('The Birds1',views.hstory2),
    path('The Tell-Tale Heart',views.hstory3),
    path('the cask of Amontillado1',views.hstory4),
    path('The landlady1',views.hstory5),
    path('The lottery',views.hstory6),
    path('The most Dangerous Game1',views.hstory7),
    path('The Monkeys paw1',views.hstory8),
    path('The open winndow1',views.hstory9),
    path('The Adventure of the Engineers Turn',views.mystery1),
    path('The Hound of the Hovervilles',views.mystery2),
    path('The Lady or the Tiger',views.mystery3),
    path('The Murders in the Rue Morgue',views.mystery4),
    path('The Purloined letter',views.mystery5),
    path('Nightfall',views.sf1),
    path('Story of your life',views.sf2),
    path('The Last Question',views.sf3),
    path('The lottery of babylon',views.sf4),
    path('The Ones who walk away from Omelas',views.sf5),
    path('The Veld',views.sf6),
    path('Northern Star',views.ad1),
    path('The Lost city of Emberstone',views.ad2),
    path('The Time Key',views.ad3),
    path('The Quest of the Sunken City',views.ad4),
    path('Whispers of the Ancient Forest',views.ad5),
    path('Operation Shadow Hawk',views.ac1),
    path('Escape from Alcatraz 2.0',views.ac2),
    path('The Dragons Den',views.ac3),
    path('Rescue at Raven Rock',views.ac4),
    path('Operation Desert Storm',views.ac5),
    path('The Lost Kingdom',views.f1),
    path('The Enchanted Forest',views.f2),
    path('The Dragons Gambit',views.f3),
    path('The Heist',views.f4),
    path('The Enchanted Grove',views.f5),



    path('launch_game/<str:game_name>/', views.launch_game, name='launch_game'),

]



