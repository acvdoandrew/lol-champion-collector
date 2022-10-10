from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('mains/', views.main_champs),
    path('mains/<int:champ_id>', views.champ_detail, name='detail')
]