from django.contrib import admin

# Register your models here.
from . models import Die, Rolls, Condition

admin.site.register(Die)
admin.site.register(Rolls)
admin.site.register(Condition)
