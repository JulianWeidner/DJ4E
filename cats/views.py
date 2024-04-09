from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from .models import Cat, Breed
from .forms import CatForm, BreedForm

# Create your views here.
class MainView(LoginRequiredMixin, ListView):
    template_name = 'cats/main.html'
    model = Cat

class CreateCatView(LoginRequiredMixin, CreateView):
    model = Cat
    form_class = CatForm
    template_name = 'cats/forms/cat_form.html'
    success_url = reverse_lazy('cats:main')
    
class DetailsCatView(LoginRequiredMixin, DetailView):
    model = Cat
    template_name = 'cats/cat_details.html'

class UpdateCatView(LoginRequiredMixin, UpdateView):
    model = Cat
    form_class = CatForm
    template_name = 'cats/forms/cat_form.html'
    success_url = reverse_lazy('cats:main')


class DeleteCatView(LoginRequiredMixin, DeleteView):
    model = Cat
    template_name = 'cats/forms/delete_form.html'
    success_url = reverse_lazy('cats:main')




class ListBreedView(LoginRequiredMixin, ListView):
    model = Breed

class CreateBreedView(LoginRequiredMixin, CreateView):
    model = Breed
    form_class = BreedForm
    template_name = 'cats/forms/breed_form.html'
    success_url = reverse_lazy('cats:main')

class DetailsBreedView(LoginRequiredMixin, DetailView):
    model = Breed

class UpdateBreedView(LoginRequiredMixin, UpdateView):
    model = Breed
    form_class = BreedForm
    template_name = 'cats/forms/breed_form.html'
    success_url = reverse_lazy('cats:main')

class DeleteBreedView(LoginRequiredMixin, DeleteView):
    model = Breed
    template_name = 'cats/forms/delete_form.html'
    success_url = reverse_lazy('cats:main')






