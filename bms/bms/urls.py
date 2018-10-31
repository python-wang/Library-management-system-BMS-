"""bms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path

from book import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),
    path('index/', views.index),
    path('books/add/', views.add),
    path('books/manage/', views.manage),
    re_path('books/delete/(?P<id>\d+)', views.delete),
    re_path('books/modify/(?P<id>\d+)', views.modify),
]
