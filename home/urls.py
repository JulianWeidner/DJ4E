from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('login/', LoginView.as_view(), name='login')
]