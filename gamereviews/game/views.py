from django.shortcuts import render, get_object_or_404
from .models import Game
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'game/index.html')

def game(request):
    game_list=Game.objects.all()
    return render(request, 'game/games.html', {'game_list': game_list})

def gameDetail(request, id):
    game=get_object_or_404(Game, pk=id)
    return render(request, 'game/gamedetail.html', {'game': game})
