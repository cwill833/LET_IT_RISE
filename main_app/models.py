from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.

class Starter(models.Model):
    name = models.CharField(max_length=100)
    temp = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Leaven(models.Model):
    time = models.CharField(max_length=200)
    temp = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starter = models.ForeignKey(Starter, on_delete=models.CASCADE)

    def __str__(self):
        return self.time

class Rise(models.Model):
    time = models.CharField(max_length=200)
    temp = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starter = models.ForeignKey(Starter, on_delete=models.CASCADE)

    def __str__(self):
        return self.time

# class Bake(models.Model):
#     start = models.DateField('start date')
#     temp = models.CharField(max_length=100)
#     lid_on = models.CharField(max_length=200)
#     lid_off = models.CharField(max_length=200)

#     def __str__(self):
#         return self.start
