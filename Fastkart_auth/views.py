from django.shortcuts import render, redirect

# Create your views here.

def signup(request):
    return render(request, "auth/signup.html")


def handlelogin(request):
    return render(request, "auth/login.html")


def handlelogout(request):
    return redirect('index.html')