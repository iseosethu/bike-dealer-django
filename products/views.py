# products/views.py
from django.views.generic import ListView
from .models import Product
from django.shortcuts import render

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'