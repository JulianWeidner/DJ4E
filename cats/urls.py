from django.urls import path
from . import views

app_name = 'cats'

urlpatterns = [
    path("", views.MainView.as_view(), name='main'),
    path("create/", views.CreateCatView.as_view(), name='cat_create'),
    path("<int:pk>/details/", views.DetailsCatView.as_view(), name='cat_details'),
    path("<int:pk>/update/", views.UpdateCatView.as_view(), name='cat_update'),
    path("<int:pk>/delete/", views.DeleteCatView.as_view(), name ='cat_delete'),


    path("breed/create/", views.CreateBreedView.as_view(), name='breed_create'),
    path("breed/", views.ListBreedView.as_view(), name='breed_list'),
    path("breed/<int:pk>/update/", views.UpdateBreedView.as_view(), name='breed_update'),
    path("breed/<int:pk>/delete", views.DeleteBreedView.as_view(), name='breed_delete')
]