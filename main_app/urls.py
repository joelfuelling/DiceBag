from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('die/', views.die_index, name='index'),
  path('die/<int:die_id>/', views.die_detail, name='detail'),
]