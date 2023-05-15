from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('die/', views.DieList.as_view(), name='index'),
  path('die/create', views.DieCreate.as_view(), name='die_create'),
  path('die/<int:pk>/', views.DieDetail.as_view(), name='die_detail'), #pk is only needed for the default classbased bview (.av_view())
  path('die/<int:pk>/update/', views.DieUpdate.as_view(), name ='die_update'),
  path('die/<int:pk>/delete/', views.DieDelete.as_view(), name ='die_delete'),
  path('die/<int:pk>/add_result', views.add_result, name='add_result'),
  path('condition/<int:die_id>/assoc_condition/<int:condition_id>/', views.assoc_condition, name='assoc_condition'),
  path('condition/<int:die_id>/remove_condition/<int:condition_id>/', views.remove_condition, name='remove_condition'),
  path('condition/', views.ConditionList.as_view(), name='condition_index'),
  path('condition/<int:pk>/', views.ConditionDetail.as_view(), name='condition_detail'),
  path('condition/create/', views.ConditionCreate.as_view(), name='condition_create'),
] 