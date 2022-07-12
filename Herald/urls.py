"""Herald URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('home/',views.home,name="Home"),
    path('home.html',views.home,name="Home"),
    path('bit.html',views.bit,name='BIT'),
    path('bit/',views.bit,name='BIT'),
    path('bibm.html',views.bibm,name='BIBM'),
    path('bibm/',views.bibm,name='BIBM'),
    path('events.html',views.events,name='events'),
    path('events/',views.events,name='events'),
    path('galleries.html',views.galleries,name='galleries'),
    path('galleries/',views.galleries,name='galleries'),
    path('contact.html', views.contactpage,name="contact"),
]
