from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('die/', views.DieList.as_view(), name='index'),
  path('die/create', views.DieCreate.as_view(), name='die_create'),
  path('die/<int:pk>/', views.DieDetail.as_view(), name='die_detail'),
  path('die/<int:pk>/update/', views.DieUpdate.as_view(), name ='die_update'),
  path('die/<int:pk>/delete/', views.DieDelete.as_view(), name ='die_delete'),
]