from django.forms import ModelForm
from .models import Leaven, Starter, Rise, Bake

class BakeForm(ModelForm):
  class Meta:
    model = Bake
    fields = ['time', 'temp']

class RiseForm(ModelForm):
  class Meta:
    model = Rise
    fields = ['time', 'temp']

class LeavenForm(ModelForm):
  class Meta:
    model = Leaven
    fields = ['time', 'temp']

class StarterForm(ModelForm):
  class Meta:
    model = Starter
    fields = ['name', 'temp']