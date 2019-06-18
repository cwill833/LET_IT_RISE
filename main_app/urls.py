from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('tools/', views.tools, name='tools'),
    path('starters1/', views.starters1, name='starters1'),
    path('starters2/', views.starters2, name='starters2'),

    path('starters/create/', views.StarterCreate.as_view(), name='starter_create'),
    path('leavens/create/', views.LeavenCreate.as_view(), name='leaven_create'),
    path('rise/create/', views.RiseCreate.as_view(), name='rise_create'),
    path('stepfive/', views.stepfive, name='stepfive'),

    path('starters3/', views.starters3, name='starters3'),
    path('leavens/', views.leavens_detail, name='leavens_detail'),
    path('mixes/', views.mixes_detail, name='mixes_detail'),
    path('fermentations/', views.fermentations_detail, name='fermentations_detail'),
    path('shapes/', views.shapes_detail, name='shapes_detail'),
    path('bakes/', views.bakes_detail, name='bakes_detail'),
    path('trackers/', views.trackers_index, name='trackers_index'),
]