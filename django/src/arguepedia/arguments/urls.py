"""arguepedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
argument_post_detail_view,
argument_post_list_view,
argument_post_create_view,
argument_post_update_view,
argument_post_delete_view

)
urlpatterns = [
    path('', argument_post_list_view),

	path('<int:post_id>/', argument_post_detail_view),
    path('argument-new/', argument_post_create_view),
    path('<int:post_id>/delete/', argument_post_delete_view),
    path('<int:post_id>/edit/', argument_post_update_view),
]
