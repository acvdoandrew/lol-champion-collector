from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('champions/', views.ChampionList.as_view(), name='champions_index'),
    path('champions/<int:pk>/', views.ChampionDetail.as_view(), name='champions_detail'),
    path('champions/create/', views.ChampionCreate.as_view(), name='champions_create'),
    path('champions/<int:pk>/update/', views.ChampionUpdate.as_view(), name='champions_update'),
    path('champions/<int:pk>/delete/', views.ChampionDelete.as_view(), name='champions_delete'),
]