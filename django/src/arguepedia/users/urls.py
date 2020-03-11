from django.contrib import admin
from django.urls import path, include
from . views import signup_view

urlpatterns = [
path('', include('django.contrib.auth.urls')),
path('signup/', signup_view),

]