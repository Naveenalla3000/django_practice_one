from django.shortcuts import render,HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("index page")

def about(req):
    return HttpResponse("about page")

def services(req):
    return HttpResponse("services page")

def contact(req):
    return HttpResponse("contact page")

def login(req):
    return HttpResponse("login page")

def signup(req):
    return HttpResponse("signup page")

def logout(req):
    return HttpResponse("logout page")

def profile(req):
    return HttpResponse("profile page")
