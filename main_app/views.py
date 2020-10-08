from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello there fellow traveler!</h1>')

def about(request):
    return render(request, 'about.html')

def semantic(request):
    return render(request, 'semantic.html')
