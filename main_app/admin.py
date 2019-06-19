from django.contrib import admin
from .models import Starter, Rise, Leaven, Bake
# Register your models here.

admin.site.register(Starter)
admin.site.register(Leaven)
admin.site.register(Rise)
admin.site.register(Bake)