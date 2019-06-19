from django.forms import ModelForm
from .models import Leaven, Starter

class LeavenForm(ModelForm):
  class Meta:
    model = Leaven
    fields = ['time', 'temp']

class StarterForm(ModelForm):
  class Meta:
    model = Starter
    fields = ['name', 'temp']