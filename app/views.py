from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import TemplateView,ListView

class home(TemplateView):
    template_name='app/home.html'


class school_list(ListView):
    model=Scholl
    template_name='app/school_list.html'
    context_object_name='schools'