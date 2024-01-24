from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib.auth import login
from django.contrib import messages

# User Profile
def profile(request):
    context = {}
    return render(request, 'user/profile.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Successfully created account for {user.email}!")
            return redirect('homepage')
    else:
        form = UserSignUpForm()
    context = {'form':form}
    return render(request, 'registration/sign_up.html', context)