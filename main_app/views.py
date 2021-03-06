from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Starter, Rise, Leaven, Bake
from .forms import LeavenForm, StarterForm, RiseForm, BakeForm

def home(request):
  return render(request, 'home.html')


def stepone(request):
  return render(request, 'starters/stepone.html')

class StarterCreate(LoginRequiredMixin, CreateView):
  model = Starter
  fields = ['name', 'temp']
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  success_url = '/stepthree/'

@login_required
def stepthree(request):
  starter = Starter.objects.filter(user = request.user).order_by('-pk')[0]
  return render(request, 'starters/stepthree.html', {'starter': starter})

@login_required
def stepfour(request, starter_id):
  starter = Starter.objects.get(id=starter_id)
  leaven_form = LeavenForm()
  return render(request, 'starters/stepfour.html', {'starter': starter, 'leaven_form': leaven_form})

@login_required
def add_leaven(request, starter_id):
	# create the ModelForm using the data in request.POST
  form = LeavenForm(request.POST)
  # validate the form
  if form.is_valid():
    leaven = form.save(commit=False)
    leaven.starter_id = starter_id
    leaven.save()
  return redirect('stepfive')

@login_required
def stepfive(request):
  starter = Starter.objects.filter(user = request.user).order_by('-pk')[0]
  return render(request, 'starters/stepfive.html', {'starter': starter})

@login_required
def stepsix(request, starter_id):
  starter = Starter.objects.get(id=starter_id)
  rise_form = RiseForm()
  return render(request, 'starters/stepsix.html', {'starter': starter, 'rise_form': rise_form})

@login_required
def add_rise(request, starter_id):
	# create the ModelForm using the data in request.POST
  form = RiseForm(request.POST)
  # validate the form
  if form.is_valid():
    rise= form.save(commit=False)
    rise.starter_id = starter_id
    rise.save()
  return redirect('stepseven')

@login_required
def stepseven(request):
  starter = Starter.objects.filter(user = request.user).order_by('-pk')[0]
  return render(request, 'starters/stepseven.html', {'starter': starter})

@login_required
def stepeight(request, starter_id):
  starter = Starter.objects.get(id=starter_id)
  bake_form = BakeForm()
  return render(request, 'starters/stepeight.html', {'starter': starter, 'bake_form': bake_form})

@login_required
def add_bake(request, starter_id):
	# create the ModelForm using the data in request.POST
  form = BakeForm(request.POST)
  # validate the form
  if form.is_valid():
    bake = form.save(commit=False)
    bake.starter_id = starter_id
    bake.save()
  return redirect('finished', starter_id=starter_id)

@login_required
def finished(request, starter_id):
  starter = Starter.objects.get(id=starter_id)
  leaven = Leaven.objects.get(starter_id=starter_id)
  rise = Rise.objects.get(starter_id=starter_id)
  bake = Bake.objects.get(starter_id=starter_id)
  return render(request, 'starters/finished.html', {
    'starter': starter,
    'leaven': leaven,
    'rise': rise,
    'bake': bake,
  })

@login_required
def index(request):
  starter = Starter.objects.filter(user = request.user)
  return render(request, 'starters/index.html', {
    'starter': starter,
  })

@login_required
def detail(request, starter_id):
  starter = Starter.objects.get(id=starter_id)
  leaven = Leaven.objects.get(starter_id=starter_id)
  rise = Rise.objects.get(starter_id=starter_id)
  bake = Bake.objects.get(starter_id=starter_id)
  return render(request, 'starters/detail.html', {
    'starter': starter,
    'leaven': leaven,
    'rise': rise,
    'bake': bake,
  })

class StarterUpdate(LoginRequiredMixin, UpdateView):
  model = Starter
  fields = ['name']
  success_url = '/index/'

class StarterDelete(LoginRequiredMixin, DeleteView):
  model = Starter
  success_url = '/index/'

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