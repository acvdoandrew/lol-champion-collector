from django.shortcuts import redirect, render
from .models import Champion, SkinTheme
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import MatchesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def add_match(request, pk):
    form = MatchesForm(request.POST)
    if form.is_valid():
        new_match = form.save(commit=False)
        new_match.champion_id = pk
        new_match.save()
    return redirect('champions_detail', pk=pk)

@login_required
def assoc_skin(request, pk, skin_id):
    Champion.objects.get(id=pk).skins.add(skin_id)
    return redirect('champions_detail', pk=pk)

def signup(request):
    error_message = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('champions_index')
        else:
            error_message = 'Signup input invalid - Please try again'
    form = UserCreationForm()
    context = {'form': form, 'error': error_message}
    return render(request, 'registration/signup.html', context)

class ChampionList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        user = self.request.user
        return Champion.objects.filter(user=user)

class ChampionDetail(LoginRequiredMixin, DetailView):
    model = Champion

    def get_context_data(self, *args, **kwargs):
        context = super(ChampionDetail, self).get_context_data(*args, **kwargs)
        matches_form = MatchesForm()
        champion = self.get_object()
        skins_not_assoc = SkinTheme.objects.exclude(id__in = champion.skins.all().values_list('id'))
        context['matches_form'] = matches_form
        context['skins'] = skins_not_assoc
        return context

class ChampionCreate(LoginRequiredMixin, CreateView):
    model = Champion
    fields = ('name', 'role', 'epithet', 'hours')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChampionUpdate(LoginRequiredMixin, UpdateView):
    model = Champion
    fields = '__all__'

class ChampionDelete(LoginRequiredMixin, DeleteView):
    model = Champion
    success_url = '/champions/'

class SkinList(LoginRequiredMixin, ListView):
    model = SkinTheme

class SkinCreate(LoginRequiredMixin, CreateView):
    model = SkinTheme
    fields = '__all__'

class SkinDetail(LoginRequiredMixin, DetailView):
    model = SkinTheme

class SkinUpdate(LoginRequiredMixin, UpdateView):
    model = SkinTheme
    fields = '__all__'

class SkinDelete(LoginRequiredMixin, DeleteView):
    model = SkinTheme
    success_url = '/skins/'