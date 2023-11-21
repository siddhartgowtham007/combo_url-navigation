from django.shortcuts import render

# Create your views here.

def speedy(request):
    return render(request,'speedy.html')

def spidy(request):
    return render(request,'spidy.html')