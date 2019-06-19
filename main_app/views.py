from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView
from .models import Starter, Rise, Leaven


def home(request):
  return render(request, 'home.html')

def bakes_detail(request):
  return render(request, 'bakes/detail.html') 

def fermentations_detail(request):
  return render(request, 'fermentations/detail.html')

class RiseCreate(CreateView):
  model = Rise
  fields = ['time', 'temp']
  success_url = '/' 

def leavens_detail(request):
  return render(request, 'leavens/detail.html')

class LeavenCreate(CreateView):
  model = Leaven
<<<<<<< HEAD
  fields = ['name', 'temp']
  success_url = '/leavens/'  
=======
  fields = ['time', 'temp']
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  success_url = '/stepfive/'  

def stepfive(request):
  return render(request, 'starters/stepfive.html')
>>>>>>> 562201428731b1f305a0766f456b5699dd90f9e5

def mixes_detail(request):
  return render(request, 'mixes/detail.html')

def shapes_detail(request):
  return render(request, 'shapes/detail.html')

def starters1(request):
  return render(request, 'starters/dayone.html')

def starters2(request):
  return render(request, 'starters/daytwo.html')

class StarterCreate(CreateView):
  model = Starter
  fields = ['name', 'temp']
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  success_url = '/starters3/'

def starters3(request):
  return render(request, 'starters/daythree.html')

def trackers_index(request):
  return render(request, 'trackers/detail.html')

def tools(request):
  return render(request, 'tools.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)