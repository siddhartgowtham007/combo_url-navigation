from django.shortcuts import render

# Create your views here.

def muscle(request):
    return render(request,'muscle.html')

def mustang(request):
    return render(request,'mustang.html')