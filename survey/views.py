from django.shortcuts import render, get_object_or_404,redirect
from django.utils.dateparse import parse_duration
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    # Your code here
    return render(request, 'index.html')

def bmi(request):
    # Your code here
    return render(request, 'bmi.html')

def dashboard(request):
    # Your code here
    return render(request, 'dashboard.html')

def household(request):
    # Your code here
    return render(request, 'household.html')

def medical_hipa(request):
    # Your code here
    return render(request, 'medical_hipa.html')
def aboutus(request):
    # Your code here
    return render(request, 'aboutus.html')

def contact(request):
    # Your code here
    return render(request, 'contact.html')

def terms(request):
    # Your code here
    return render(request, 'terms.html')
def privacy(request):
    # Your code here
    return render(request, 'privacy.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        # Check if passwords match
        if password == password1:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            # Check if email already exists
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered')
                return redirect('register')
            else:
                # Create the user
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate( username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')     


def profile(request):
    return render(request, 'profile.html')


@login_required # type: ignore
def profile(request):
    return render(request, 'profile.html')

@login_required # type: ignore
def edit_profile(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        request.user.save()
        
        messages.success(request, 'Your profile has been updated!')
        return redirect('profile')
        
    return render(request, 'accounts/edit_profile.html')
   


# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User

# @login_required
# def dashboard(request):
#     try:
#         user = request.user
#         user_type = user.user_type if hasattr(user, 'user_type') else 'default_type'  # Replace 'default_type' with your default type
#         return render(request, 'dashboard.html', {'user_type': user_type})
#     except User.DoesNotExist:
#         # Handle the case where the user does not exist
#         return redirect('register')  # or another appropriate view
