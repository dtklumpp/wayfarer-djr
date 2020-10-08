from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import User_Form
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello there fellow traveler!</h1>')

def about(request):
    user_form = User_Form()
    context = {'form': user_form}
    return render(request, 'about.html', context)

def semantic(request):
    return render(request, 'semantic.html')

def signup(request):
    # if post
    if request.method == "POST":
        # build out data from form
        username_form = request.POST['username']
        email_form = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # validate that passwords match
        if password == password2:
        # check if username exists in db
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username is already taken.'}
                return render(request, 'register.html', context)
            else:
                if User.objects.filter(email=email_form).exists():
                    context = {'error':'That email already exists.'}
                    return render(request, 'register.html', context)
                else: 
                # if everything is ok create account
                    user = User.objects.create_user(
                        username=username_form, 
                        email=email_form, 
                        password=password)
                    user.save()
                    send_mail(
                        'Welcome Wayfarer!', 
                        'You are registered! Feel free to add your travel experiences and tips to our community of travellers!',
                        'wwayfarer25@gmail.com',
                        f"{email}"
                        )
                    # TODO redirect to correct destination
                    return redirect('/about/')
        else:
            context = {'error':'Passwords do not match'}
            return render(request, 'register.html', context)
    else:
        # if not post send message, try again 
        context = {'error':'Your account was not created. Please try again.'}
        return redirect(request, '/about/')