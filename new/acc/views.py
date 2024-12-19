from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def nextone(request):
    return render(request, 'nextone.html')
