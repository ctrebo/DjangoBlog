# Django Blog Application

## The goal of this python project is to have a python blog applicaton which can be used as Blog App

## Technologies
Project is created with:

* Python
* Django
* Pillow
* OS library
* datetime library

## Prerequisites

* Python
* git

## Setup

To run this project first install some libraries via pip:
```
pip install django Pillow
```

clone repository in new made folder
```
git clone https://github.com/ctrebo/DjangoBlog
```

open blog/settings.py, delete line 16 and 17. Then in settings.py search 'SECRET_KEY' and replace ´´´str(os.getenv('SECRET_KEY'))´´´ with the secret key of your choice

go to the project root and run migrations
```
python manage.py migrate
```

at the end start the server
```
python manage.py runserver
```