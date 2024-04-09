from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MainView(LoginRequiredMixin, View):
    template_name = 'cats/main.html'
    
    def get(self, request):
        return render(request, self.template_name)
