from django.shortcuts import render, httpResponse, render_to_response

# Create your views here.

def home (request):
    return render_to_response("home.html")

def about (request):
    return render_to_response("about.html")

def contact_us (request):
    return render_to_response("contact_us.html")

def category (request):
    return render_to_response("caterory.html")
