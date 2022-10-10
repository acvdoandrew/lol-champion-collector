from django.shortcuts import render
from .models import Champion

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def main_champs(request):
    mains = Champion.objects.all()
    return render(request, 'champs/mains.html', { 'mains': mains })

def champ_detail(request, champ_id):
    champ = Champion.objects.get(id=champ_id)
    return render(request, 'champs/detail.html', {'champ': champ})