from django.contrib import admin

# Register your models here.
from .models import ArgumentPost, Action, Category

admin.site.register(ArgumentPost)
admin.site.register(Category)

admin.site.register(Action)
