from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth.decorators import login_required

def Homepage(request):
    return render(request, 'homepage.html')

def AboutPage(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # Redirect to login page after successful sign-up
        else:
            messages.error(request, "There was an error creating your account.")  # Error message if form is invalid
    else:
        form = UserSignupForm()  # Empty form for GET request

    return render(request, 'signup.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate user and log them in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, "You have logged in successfully!")
                return redirect('upload')  # Redirect to the upload page after successful login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def uploadPage(request):
    # Your upload page logic here
    return render(request, 'upload.html')