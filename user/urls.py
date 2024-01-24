from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('user/profile/', views.profile, name='profile'),
    path('user/sign_up/', views.sign_up, name='sign_up'),
]
