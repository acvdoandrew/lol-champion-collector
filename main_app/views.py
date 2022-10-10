from django.shortcuts import render
from .models import Champion
from django.views.generic import ListView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class ChampionList(ListView):
    model = Champion

def champ_detail(request, champ_id):
    champ = Champion.objects.get(id=champ_id)
    return render(request, 'champs/detail.html', {'champ': champ})