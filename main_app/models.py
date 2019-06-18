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

# class Progress(models.Model):
#     page = models.CharField(max_length=200)

# class Comment(models.Model):
#     description = models.TextField(max_length=250)


class Leaven(models.Model):
    start = models.DateField('start date')
    time = models.CharField(max_length=200)
    temp = models.CharField(max_length=100)
    starter = models.ForeignKey(Starter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.start

# class Rise(models.Model):
#     start = models.DateField('start date')
#     time = models.CharField(max_length=200)
#     temp = models.CharField(max_length=100)

#     def __str__(self):
#         return self.start

# class Bake(models.Model):
#     start = models.DateField('start date')
#     temp = models.CharField(max_length=100)
#     lid_on = models.CharField(max_length=200)
#     lid_off = models.CharField(max_length=200)

#     def __str__(self):
#         return self.start
