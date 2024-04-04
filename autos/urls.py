from . import urls
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'autos'

urlpatterns = [
    path('autos/', views.AutosListView.as_view(), name='autos_list_view'),
    #path('autos/list', views.AutosListView.as_view(), name = 'autos_list_view'),
    path('autos/create/', views.AutosCreateView.as_view(), name = 'autos_create_view'), #Create
    path('autos/<int:pk>/', views.AutosDetailView.as_view(), name = 'autos_detail_view'), #Read,
    path('autos/<int:pk>/update/', views.AutosUpdateView.as_view(), name = 'autos_update_view'), #update
    path('autos/<int:pk>/delete/', views.AutosDeleteView.as_view(), name = 'autos_delete_view'), #delete

    path('autos/makes/', views.MakeListView.as_view(), name = "makes_list_view"), #list
    path('autos/makes/create/', views.MakeCreateView.as_view(), name='makes_create_view'),
    #path('autos/makes/<int:pk>/'),
    path('autos/makes/<int:pk>/update/', views.MakeUpdateView.as_view(), name='makes_update_view'),
    path('autos/makes/<int:pk>/delete/', views.MakeDeleteView.as_view(), name='makes_delete_view'),

]