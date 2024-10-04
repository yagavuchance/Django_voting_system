from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to login after successful signup
        else:
            # If the form is invalid, return to the signup page with the form errors
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'users/signup.html', {'form': form})

def login_user(request):
    form = AuthenticationForm()  # Initialize the form first
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  # Pass the POST data to the form
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {username}, you have successfully logged in!")
                return redirect('index')  # Redirect to the desired page after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    if request.method =="POST":
        logout(request)
        messages.success(request, "logged out successfuly")
        return redirect('index')
    
