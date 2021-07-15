from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.register, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('signin/', auth_views.LoginView.as_view(template_name='user/signin.html'), name="signin"),
    path('signout/', auth_views.LogoutView.as_view(template_name='user/signout.html'), name="signout"),


]
