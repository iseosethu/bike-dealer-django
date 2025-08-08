# core/urls.py
from django.urls import path
from .views import (
    HomeView, 
    AboutView, 
    ContactView, 
    BranchesView, 
    BookServiceView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('branches/', BranchesView.as_view(), name='branches'),
    path('book-service/', BookServiceView.as_view(), name='book_service'),
]