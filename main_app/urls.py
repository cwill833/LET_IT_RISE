from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tools/', views.tools, name='tools'),
    path('accounts/signup', views.signup, name='signup'),
    path('starters/', views.starters_detail, name='starters_detail'),
    path('leavens/', views.leavens_detail, name='leavens_detail'),
    path('mixes/', views.mixes_detail, name='mixes_detail'),
    path('fermentations/', views.fermentations_detail, name='fermentations_detail'),
    path('shapes/', views.shapes_detail, name='shapes_detail'),
    path('bakes/', views.bakes_detail, name='bakes_detail'),
    path('trackers/', views.trackers_index, name='trackers_index'),
]