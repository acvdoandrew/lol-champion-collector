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

def assoc_skin(request, pk, skin_id):
    Champion.objects.get(id=pk).skins.add(skin_id)
    return redirect('champions_detail', pk=pk)

class ChampionList(ListView):
    model = Champion

class ChampionDetail(DetailView):
    model = Champion

    def get_context_data(self, *args, **kwargs):
        context = super(ChampionDetail, self).get_context_data(*args, **kwargs)
        matches_form = MatchesForm()
        champion = self.get_object()
        skins_not_assoc = SkinTheme.objects.exclude(id__in = champion.skins.all().values_list('id'))
        context['matches_form'] = matches_form
        context['skins'] = skins_not_assoc
        return context

class ChampionCreate(CreateView):
    model = Champion
    fields = ('name', 'role', 'epithet', 'hours')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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