from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('stepone/', views.stepone, name='stepone'),
    path('steptwo/create/', views.StarterCreate.as_view(), name='starter_create'),
    path('stepthree/', views.stepthree, name='stepthree'),
    path('stepfour/<int:starter_id>/', views.stepfour, name='stepfour'),
    path('stepfour/<int:starter_id>/add_leaven/', views.add_leaven, name='add_leaven'),
    path('stepfive/', views.stepfive, name='stepfive'),
    path('stepsix/<int:starter_id>/', views.stepsix, name='stepsix'),
    path('stepsix/<int:starter_id>/add_rise/', views.add_rise, name='add_rise'),
    path('stepseven/', views.stepseven, name='stepseven'),
    path('stepeight/<int:starter_id>/', views.stepeight, name='stepeight'),
    path('stepeight/<int:starter_id>/add_bake/', views.add_bake, name='add_bake'),
    path('finished/<int:starter_id>/', views.finished, name='finished'),
    path('index/', views.index, name='index'),
    path('detail/<int:starter_id>/', views.detail, name='detail'),
    path('starter/<int:pk>/update/', views.StarterUpdate.as_view(), name='starter_update'),
    path('starter/<int:pk>/delete/', views.StarterDelete.as_view(), name='starter_delete'),
]