from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name  ='index.html'

class NowtView(TemplateView):
  template_name = '404.html'
class ServerErrorView(TemplateView):
    template_name='500.html'


# Create your views here.
