from django.shortcuts import render

# User Profile
def profile(request):
    context = {}
    return render(request, 'user/profile.html', context)

def sign_up(request):
    context = {}
    return render(request, 'registration/sign_up.html', context)
