from django.shortcuts import render
from .models import Champion
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class ChampionList(ListView):
    model = Champion

class ChampionDetail(DetailView):
    model = Champion

class ChampionCreate(CreateView):
    model = Champion
    fields = '__all__'

class ChampionUpdate(UpdateView):
    model = Champion
    fields = '__all__'
