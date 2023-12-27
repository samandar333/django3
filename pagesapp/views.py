from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomepageView(TemplateView):
    template_name = 'homepages.html'

class AboutpageView(TemplateView):
    template_name = 'aboutpage.html'
