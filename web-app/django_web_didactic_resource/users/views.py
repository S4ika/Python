from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def auth(request): #аргумент request обязательный
    return render(request, 'users/auth.html')

def reg(request): #аргумент request обязательный
    return render(request, 'users/reg.html')