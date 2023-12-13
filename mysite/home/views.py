from django.shortcuts import render,HttpResponse

# Create your views here.
def index(req):
    # return HttpResponse("index page")
    context = {
        'id': 1,
        'name': "Alax",
        'designation': "admin",
        'salary': 50000,
        'status':'good',
        'project':['alax','alaxa','naxel',''],
        'address':{
            'city':'WASILLA AK 99567-5448chi',
            'country':'USA'
        },
        'skills':['sleeping',
                  'eating',
                  'sleeping more',
                  'late wake up',
                  'again sleeping'],
        'hobbies':[
            {
                "work":'sleeping',
                "rank":1
            },
            {
                "work":'eating',
                "rank":2
            },
            {
                "work":'sleeping more',
                "rank":3
            },
            {
                "work":'dreaming',
                "rank":4
            },
            {
                "work":"thinking",
                "rank":8
            },
        ],
    }
    return render(req,"index.htmx",context)

def about(req):
    # return HttpResponse("about page")
    return render(req,"about.htmx")

def services(req):
    # return HttpResponse("services page")
    return render(req,"services.htmx")

def contact(req):
    # return HttpResponse("contact page")
    return render(req,"contact.htmx")

def login(req):
    return HttpResponse("login page")

def signup(req):
    return HttpResponse("signup page")

def logout(req):
    return HttpResponse("logout page")

def profile(req):
    return HttpResponse("profile page")
