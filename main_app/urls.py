from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),


    path('stepone/', views.stepone, name='stepone'),

    # path('steptwo/', views.steptwo, name='steptwo'), #skips this for now
    
    path('steptwo/create/', views.StarterCreate.as_view(), name='starter_create'),

    path('stepthree/', views.stepthree, name='stepthree'),

    # path('starters2/', views.starters2, name='starters2'),

    path('stepfour/<int:starter_id>/', views.stepfour, name='stepfour'),

    # path('stepfour/<int:starter_id>/add_leaven/', views.LeavenCreate.as_view(), name='leaven_create'),

    path('stepfour/<int:starter_id>/add_leaven/', views.add_leaven, name='add_leaven'),

    path('stepfive/', views.stepfive, name='stepfive'),

    path('stepsix/<int:starter_id>/', views.stepsix, name='stepsix'),

    path('stepsix/<int:starter_id>/add_rise/', views.add_rise, name='add_rise'),

    path('stepseven/', views.stepseven, name='stepseven'),

    path('stepeight/<int:starter_id>/', views.stepeight, name='stepeight'),

    path('stepeight/<int:starter_id>/add_bake/', views.add_bake, name='add_bake'),

    # path('rise/create/', views.RiseCreate.as_view(), name='rise_create'),

    path('finished/<int:starter_id>/', views.finished, name='finished'),

    path('index/', views.index, name='index'),

    path('detail/<int:starter_id>/', views.detail, name='detail'),

    path('starter/<int:pk>/update/', views.StarterUpdate.as_view(), name='starter_update'),
    path('starter/<int:pk>/delete/', views.StarterDelete.as_view(), name='starter_delete'),





    path('leavens/', views.leavens_detail, name='leavens_detail'),
    path('tools/', views.tools, name='tools'),
    path('mixes/', views.mixes_detail, name='mixes_detail'),
    path('fermentations/', views.fermentations_detail, name='fermentations_detail'),
    path('shapes/', views.shapes_detail, name='shapes_detail'),
    path('bakes/', views.bakes_detail, name='bakes_detail'),
    path('trackers/', views.trackers_index, name='trackers_index'),


]