from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home/index.html")
    # return HttpResponse("Welcome to Home Page !")
    # return render(request, 'home/home.html')

def product(request, Product_id):
    return render(request, "home/category.html")
    # return HttpResponse(f"Welcome to Product Page . The current Product id : {Product_id}")

def old_url_redirect(request):
    return redirect('new_url')

def new_url(request):
    return HttpResponse("This is Your new URL Page")