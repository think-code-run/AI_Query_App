from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm


def Homepage(request):
    return render(request,'homepage.html')

def AboutPage(request):
    return render(request,'about.html')

def signupPage(request):
    return render(request,'signup.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})
