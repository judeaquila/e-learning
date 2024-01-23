from django.shortcuts import render

# Home Page
def homepage(request):
    context = {}
    return render(request, 'main/index.html', context)

def pricing(request):
    context = {}
    return render(request, 'main/pricing.html', context)