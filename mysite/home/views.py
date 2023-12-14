from django.shortcuts import render,HttpResponse
from home.models import Employee
from django.contrib import messages

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
                "rank":2
            },
            {
                "work":'eating',
                "rank":3
            },
            {
                "work":'sleeping more',
                "rank":4
            },
            {
                "work":'dreaming',
                "rank":5
            },
            {
                "work":"thinking",
                "rank":6
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
    if req.method == "GET":
        return render(req,"contact.htmx")
    elif req.method == "POST":
        try:
            name = req.POST.get('name')
            email = req.POST.get('email')
            phone = req.POST.get('phone')
            role = req.POST.get('role')
            if not name or not email or not phone or not role:
               raise Exception("All fields are required")
            newEmployee = Employee(emp_name = name,
                                emp_email = email,
                                emp_phno = phone,
                                emp_role = role)
        # print(newEmployee.emp_email,newEmployee.emp_name,newEmployee.emp_phno,newEmployee.emp_role,newEmployee.emp_id)
            newEmployee.save()
            messages.success(req,"Employee added successfully")
        except Exception as exc:
            print(exc)
        finally:
            return render(req,"contact.htmx")

def login(req):
    return HttpResponse("login page")

def signup(req):
    return HttpResponse("signup page")

def logout(req):
    return HttpResponse("logout page")

def profile(req):
    return HttpResponse("profile page")
