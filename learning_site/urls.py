"""learning_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url #don't forget to import include!
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #tells django/python how to serve static files

from . import views #import views file

urlpatterns = [
    url(r'^courses/', include('courses.urls', namespace='courses')), #include('courses.urls', namespace='course') to namespace a group of URLs
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page), #takes 5 arguments(pattern, view to send request to, keyword argument for view, route name, prefix) #
]

urlpatterns += staticfiles_urlpatterns()
