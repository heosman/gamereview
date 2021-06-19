from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),
    path('gameDetail/<int:id>', views.gameDetail, name='detail'),
    path('newgame/', views.newGame, name='newgame'),

]