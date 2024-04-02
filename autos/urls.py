from . import urls
from django.urls import path
from . import views

app_name = 'autos'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index')
]