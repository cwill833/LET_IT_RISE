from django.forms import ModelForm
from .models import Leaven, Starter, Rise

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