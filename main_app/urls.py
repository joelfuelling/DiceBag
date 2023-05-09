from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('die/', views.DieList.as_view(), name='index'),
  path('die/create', views.DieCreate.as_view(), name='die_create'),
  path('die/<int:die_id>/', views.die_detail, name='detail'),
]