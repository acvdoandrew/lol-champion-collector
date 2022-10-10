from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mains/', views.ChampionList.as_view(), name='mains_index'),
    path('mains/<int:pk>/', views.ChampionDetail.as_view(), name='mains_detail')
]