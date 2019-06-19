from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView
from .models import Starter, Rise, Leaven
from .forms import LeavenForm, StarterForm, RiseForm, BakeForm

def home(request):
  return render(request, 'home.html')


def stepone(request):
  return render(request, 'starters/stepone.html')

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

def stepfour(request, starter_id):
  starter = Starter.objects.get(id=starter_id)
  leaven_form = LeavenForm()
  return render(request, 'starters/stepfour.html', {'starter': starter, 'leaven_form': leaven_form})

# class LeavenCreate(CreateView):
#   model = Leaven
#   fields = ['time', 'temp']
#   success_url = '/stepfive/' 

def add_leaven(request, starter_id):
	# create the ModelForm using the data in request.POST
  form = LeavenForm(request.POST)
  # validate the form
  if form.is_valid():
    leaven = form.save(commit=False)
    leaven.starter_id = starter_id
    leaven.save()
  return redirect('stepfive')

def stepfive(request):
  starter = Starter.objects.filter(user = request.user).reverse()[0]
  return render(request, 'starters/stepfive.html', {'starter': starter})

def stepsix(request, starter_id):
  starter = Starter.objects.get(id=starter_id)
  rise_form = RiseForm()
  return render(request, 'starters/stepsix.html', {'starter': starter, 'rise_form': rise_form})

def add_rise(request, starter_id):
	# create the ModelForm using the data in request.POST
  form = RiseForm(request.POST)
  # validate the form
  if form.is_valid():
    rise= form.save(commit=False)
    rise.starter_id = starter_id
    rise.save()
  return redirect('stepseven')

def stepseven(request):
  starter = Starter.objects.filter(user = request.user).reverse()[0]
  return render(request, 'starters/stepseven.html', {'starter': starter})

def stepeight(request, starter_id):
  starter = Starter.objects.get(id=starter_id)
  bake_form = BakeForm()
  return render(request, 'starters/stepeight.html', {'starter': starter, 'bake_form': bake_form})

def add_bake(request, starter_id):
	# create the ModelForm using the data in request.POST
  form = BakeForm(request.POST)
  # validate the form
  if form.is_valid():
    bake = form.save(commit=False)
    bake.starter_id = starter_id
    bake.save()
  return redirect('stepseven')

# class RiseCreate(CreateView):
#   model = Rise
#   fields = ['time', 'temp']
#   success_url = '/stepfive/' 



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

def bakes_detail(request):
  return render(request, 'bakes/detail.html') 

def fermentations_detail(request):
  return render(request, 'fermentations/detail.html')

def trackers_index(request):
  return render(request, 'trackers/detail.html')

def tools(request):
  return render(request, 'tools.html')

def leavens_detail(request):
  return render(request, 'leavens/detail.html')

def mixes_detail(request):
  return render(request, 'mixes/detail.html')

def shapes_detail(request):
  return render(request, 'shapes/detail.html')

def finished(request):
  return render(request, 'starters/finished.html' )
