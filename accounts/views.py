from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
import re

# Create your views here.
def verify_options(request):
    return render(request, 'accounts/verify_options.html')

def login(request):
    if request.method == "POST" and 'login-btn' in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is invalid')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    if request.method == "POST" and 'signup-btn' in request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        isAdded = False

        # Check if there any empty fields
        if username and email and password and confirm_password:
            if password == confirm_password:
                # Check if any data is taken in the database
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'This username is taken')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'This email is taken')
                    else:
                        regex = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                        if re.match(regex, email):
                            user = User.objects.create_user(
                                username=username,
                                email=email,
                                password=password
                            )
                            user.save()

                            # Reset Fields
                            username = ''
                            email = ''
                            password = ''
                            confirm_password = ''

                            # Success Message
                            messages.success(request, 'Your account is created successfully')

                            isAdded = True
                        else:
                            messages.error(request, 'Invalid email address')
            else:
                messages.error(request, "Confirm password doesn't match Password")
        else:
            messages.error(request, 'Check empty fields')
        return render(request, 'accounts/signup.html', {
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'isAdded': isAdded,
        })
    else:
        return render(request, 'accounts/signup.html')
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('index')
    else:
        messages.error(request, 'User is not logged in')