from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'core/home.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactView(TemplateView):
    template_name = 'core/contact.html'

class BranchesView(TemplateView):
    template_name = 'core/branches.html'

class BookServiceView(TemplateView):
    template_name = 'core/book_service.html'