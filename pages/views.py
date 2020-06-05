from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.


class HomePgView(TemplateView):
    template_name = 'home.html'


class AboutPgView(TemplateView):
    template_name = 'about.html'
