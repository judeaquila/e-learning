from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.profile, name='profile'),
    path('user/', views.sign_up, name='sign_up'),
]
