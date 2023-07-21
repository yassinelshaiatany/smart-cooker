from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'pages/dashboard.html')
    else:
        messages.error(request, 'User is not logged in')
        return redirect('login')