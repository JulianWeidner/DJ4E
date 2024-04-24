"""
URL configuration for coursera project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.views.static import serve

import os




urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include('home.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('ads/', include('ads.urls')),
    re_path(r'^oauth/ ', include('social_django.urls', namespace='social'))
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
    path('favicon.ico', serve, {'path': 'favicon.ico', 'document_root': os.path.join(BASE_DIR, 'home/static'),} )
]


try:
    from . import github_settings
    social_login_template = 'registration/login_social.html'
    urlpatterns.insert(0, path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login_template)))
    print('Using ' + social_login_template + ' as the login template' )
except:
    print('Using registration/login.html as the login template')