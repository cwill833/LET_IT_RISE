from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView
from .models import Starter, Rise, Leaven
from .forms import LeavenForm, StarterForm

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
  fields = ['time', 'temp']
  
  success_url = '/stepfive/'  

def stepfive(request):
  return render(request, 'starters/stepfive.html')

def mixes_detail(request):
  return render(request, 'mixes/detail.html')

def shapes_detail(request):
  return render(request, 'shapes/detail.html')

def stepone(request):
  return render(request, 'starters/stepone.html')

# def steptwo(request):
# 	# create the ModelForm using the data in request.POST
#   starter_form = StarterForm()
#   form = StarterForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # don't save the form to the db until it
#     # has the cat_id assigned
#     new_starter = form.save(commit=False)
#     new_starter
#     new_starter.save()
#   return render(request, 'starters/steptwo.html')

class StarterCreate(CreateView):
  model = Starter
  fields = ['name', 'temp']
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  success_url = '/stepthree/'

def stepthree(request):
  starter = Starter.objects.filter(user = request.user).reverse()[0]
  return render(request, 'starters/stepthree.html', {'starter': starter})

def add_leaven(request, starter_id):
	# create the ModelForm using the data in request.POST
  form = LeavenForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_leaven = form.save(commit=False)
    new_leaven.starter_id = starter_id
    new_leaven.save()
  return render(request, 'stepfive', {'starter_id': starter_id})


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