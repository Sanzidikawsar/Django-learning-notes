from  django.http import request, HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse("Welcome to home page!")

def html_view(request):
    return render(request, 'index.html')