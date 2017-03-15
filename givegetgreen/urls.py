#! /usr/bin/env python2.7
"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from givegetgreen.home.views import HomeView
from givegetgreen.addPost.views import AddPostView
from givegetgreen.deletePost.views import DeletePostView
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = [
    # Homepage
    url(r'^home$', HomeView.as_view(), name='home'),
    url(r'^$', RedirectView.as_view(pattern_name='home', permanent=False)),
    url(r'^add$', AddPostView.as_view(), name='add'),
    url(r'^delete$', DeletePostView.as_view(), name='delete'),
    url(r'^admin/', include(admin.site.urls)),
]
