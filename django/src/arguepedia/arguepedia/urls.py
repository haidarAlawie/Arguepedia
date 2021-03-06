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
from django.urls import path, include
from django.conf import settings
from .views import index_page, contactus_page, graph1_page
from arguments.views import (
create_view,
)


from searches.views import search_view

urlpatterns = [
	path('', index_page, name='home'),
    path('search/', search_view),
    path('contact/', contactus_page),
    path('arguments/', include('arguments.urls'), name='arguments'),
    path('argument-new/', create_view),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),

    path('graph1', graph1_page),
    path('training/', include('training.urls')),
]


if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
