from django.shortcuts import redirect, render
from .models import Champion, SkinTheme
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import MatchesForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def add_match(request, pk):
    form = MatchesForm(request.POST)
    if form.is_valid():
        new_match = form.save(commit=False)
        new_match.champion_id = pk
        new_match.save()
    return redirect('champions_detail', pk=pk)

class ChampionList(ListView):
    model = Champion

class ChampionDetail(DetailView):
    matches_form = MatchesForm()
    model = Champion
    extra_context = {'matches_form': matches_form}

class ChampionCreate(CreateView):
    model = Champion
    fields = '__all__'

class ChampionUpdate(UpdateView):
    model = Champion
    fields = '__all__'

class ChampionDelete(DeleteView):
    model = Champion
    success_url = '/champions/'

class SkinList(ListView):
    model = SkinTheme

class SkinCreate(CreateView):
    model = SkinTheme
    fields = '__all__'

class SkinDetail(DetailView):
    model = SkinTheme

class SkinUpdate(UpdateView):
    model = SkinTheme
    fields = '__all__'

class SkinDelete(DeleteView):
    model = SkinTheme
    success_url = '/skins/'