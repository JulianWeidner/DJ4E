from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from autos.models import Autos, Make
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AutosForm, MakeForm
from .models import Autos, Make


# Create your views here.
class AutosListView(LoginRequiredMixin, ListView):
    model = Autos
    template_name = 'autos/list_auto.html'

class AutosDetailView(LoginRequiredMixin, DetailView):
    model = Autos
    template_name = 'autos/detail_auto.html'

class AutosCreateView(LoginRequiredMixin, CreateView):
    model = Autos
    form_class = AutosForm
    template_name = 'autos/form_auto.html'
    success_url = reverse_lazy('autos:autos_list_view')

class AutosUpdateView(LoginRequiredMixin, UpdateView):
    model = Autos
    template_name = 'autos/form_auto.html'
    form_class = AutosForm
    success_url = reverse_lazy('autos:autos_list_view')

class AutosDeleteView(LoginRequiredMixin, DeleteView):
    model = Autos
    template_name = 'autos/form_delete_autos.html'
    success_url = reverse_lazy('autos:autos_list_view')


class MakeListView(LoginRequiredMixin, ListView):
    model = Make
    template_name = 'autos/list_make.html'

class MakeCreateView(LoginRequiredMixin, CreateView):
    model = Make
    template_name = 'autos/form_make.html'
    form_class = MakeForm
    success_url = reverse_lazy('autos:makes_list_view')


class MakeUpdateView(LoginRequiredMixin, UpdateView):
    model = Make
    template_name = 'autos/form_make.html'
    form_class = MakeForm
    success_url = reverse_lazy('autos:makes_list_view')

class MakeDeleteView(LoginRequiredMixin, DeleteView):
    model = Make
    template_name = 'autos/form_delete_make.html'
    success_url = reverse_lazy('autos:makes_list_view')






