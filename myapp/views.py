from django.shortcuts import render
from django.views.generic import DetailView
from .models import CustomUser

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'user_profile.html'
