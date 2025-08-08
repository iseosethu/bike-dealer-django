from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import SignUpView, CustomLoginView, CustomLogoutView, ProfileView, ProfileUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='users/password_change.html'
    ), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'
    ), name='password_change_done'),
]