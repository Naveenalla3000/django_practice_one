# creating virtual environment for python project

`python -m venv myenv`
`myenv\Scripts\activate`
`pip install pipenv`
`pipenv install`
`pipenv install django`
--- optional `pipenv install pandas`



# creating a project of django

`django-admin startproject mysite`
# add runserver command in Pipfile
`[scripts]`
`dev = python mysite/manage.py runserver 8080`
--- run the run through cli

# run the server 
pipenv run dev

# creating the static and templates directories in root of project
`mkdir static && mkdir templates`
`make sure that you explictly define the static and templates directories in setting.py`
# example for static directories
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
        ],
    }
]

# test the static files like .png .jpg .txt ect..
create an test.txt(any name) and check wether we getting expected output in browser or not



# creating app
`django-admin startapp home`
# create urls.py in the home directory
`touch urls.py`
# editing the urls.py files
edit the mysite/urls.py such that make sure that you added home.urls in urlpatterns
at the same time add urlpatterns in urls.py which is at home directory.

# define the methods in home/view.py {home,about,...} and give the apporater path in home/urls.py
this is simple called as request dispatcher (we can think it as controllers)












# general description 

--- django have MVT architecture NOT controllers, we have url dispatcher (urls.py)
    M - Models - DATABASE DESIGN
    V - Views
    T - Templates - html,css and js


