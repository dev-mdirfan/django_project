# Django Project

- Building a full feature application using django framework in python.

## Feature

- Blog style application where different users can write different posts (blog posts, twitter updates etc).
- Authentication system(log in).
- Register ( create new Account).
- Login (If already have account).
- Forgot Password(Reset Password by getting an email).
- Profile, update profile, update picture profile.
- View others people posts.
- Update/Delete posts by double verification.
- Work with databases & how to create an authentication (accepts user input from and send emails to reset password etc).
- Access admin page/Nice interface.

## Need Packages

- Need to install python
- How to work with virtual environment.
- wondering how to set-up my text-editor. I have videos check out them.

### 1. Install Django

```shell
pip install django
```
- To be sure.

```shell
python -m django --version
```

- available commands provided by django.

```shell
# List of sub commands
django-admin
```

- Use `startproject`: will create a new django project here that has a complete structure with different files and everything we need to start in.

### Create project

```shell
django-admin startproject django_project
```

- If you look on your file explorer now you have a directory called `django_project`.
- Let look at the project structure what that `startproject` command just created for us.

```shell
cd django_project
```

- Open a code editor.
- Now lets look at the project structure that startproject command created for us. Let me show structure in command line interface.

```shell
tree
```

![Image](project_structure-tree-command.png)

```shell
.
|--- django_project
|     |-- __init__.py
|     |-- asgi.py
|     |-- settings.py
|     |-- urls.py
|     |-- wsgi.py
|
|--- manage.py
```

- Now we can see here in structure that on base level we have a manage.py and a `django_project` directory.
- `manage.py` is a file that allows us to run main line command & we don't want making any changes here.
- We also have a directory called `django_project` which is also the name that used in our project itself. Within this directory we have 5 different files.

`__init__.py`: It just an empty file. That just tells python this is just python package.
Next we have `settings.py` This where we have different change settings and configurations we will be using this through out series or development.

```py
# To run the server
python manage.py runserver
# you might have warning we will fix next time.
```

- localhost = 127.0.0.1

### Creating blog app

- A single project can have multiple apps like blog app, store app.

```py
# creating blog app

python manage.py startapp blog

# or

django-admin startapp store
```

- write in `blog/views.py`:

```py
# importing 
from django.http import HttpResponse

# Create our views here.

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
```

- map the url in `/blog` create a new file `urls.py` and write -

```py
from django.urls import path

from . import views

urlpatterns = [
    # creating path for blog home page
    path('', views.home, name='blog-home'),
]
```


## First Migration

- First create super user.

```py
python manage.py createsuperuser
```

- Second you change `models.py` in app.
- then commands to migrate

```py
python manage.py makemigrations

python manage.py sqlmigrate blog 0001

python manage.py migrate

python manage.py shell
```

Write in migrate shell ->

```py
from blog.models import Post
from django.contrib.auth.models import User

# See all users
User.objects.all()

# First user
User.objects.first()

# Last User
User.objects.last()

# Filter result of user
User.objects.filter(username='Irfan')

# First of filter result
User.objects.filter(username='Irfan').first()

# Store user in a variable 
user = User.objects.filter(username='Irfan').first()

# To see id of user
user.id

# Primary Key of user which is same as id
user.pk

# get user by id
user = User.objects.get(id=1)

'''
Lets create a new post which author is this user
'''

# Check all posts
Post.objects.all()

# Create post
post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
# or
post_2 = Post(title='Blog 2', content='Second Post Content!', author_id=user.id)

# after creation of post you have to save
post_1.save()
Post.objects.all()

# To exit shell
exit()

# Post save into variable
post = Post.objects.first()

# Now you can access all fields
post.content
post.date_posted
post.author
post.author.email               # grab email of author user


# general command
.modelname_set

# Get all post written by a user
user.post_set
user.post_set.all()

# Create post using post_set
user.post_set.create(title='Blog 3', content='Third Post Content!')
```

### Create users app

```py
python manage.py startapp users
```


### Crispy Forms Template

```py
pip install django-crispy-forms
```
