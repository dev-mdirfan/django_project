# Django Project

- [Django Project](#django-project)
  - [Blog Features:](#blog-features)
  - [Table of Content for Tutorial](#table-of-content-for-tutorial)
  - [First Migration](#first-migration)
    - [Create users app](#create-users-app)
    - [Crispy Forms Template](#crispy-forms-template)


Hi, we are going to learn how to build a full feature web application using django framework in python. Django is very popular framework that gives us a lots of functionality right of the box and makes very enjoyable to work with these web applications. First lets see what we are building in this series. And then get started learning how to actually put out together.

![GIF of the Project](#)

## Blog Features:

A blog style application where different users can write different posts. This can be a blog posts, twitter updates, Instagram post etc.

- We have an authentication system. Via __register__ new user can create a new account, if you have already account you can __login__ by username and password. Via __Forgot Password__ link that are allow to reset the password by getting an email. And __logout__ off course.
- User can view their __Profile__ page, update their profile information like - update username, update profile picture and that also resize in background to save picture in web server if that picture too large.
- On __Home__ page, you can view others people posts. Some post that you have written then you can modify or delete that post.
- Ability to Update/Delete that posts by double confirmation.
- Building something like this is great way to learn engine out of the framework because you gonna be exposed so many different things for example we learn how to work with databases & how to create an authentication system and (accepts user input from  __forms__ and send emails to reset password etc).
- Since this is __Django__ application we also have to ability to access admin page/Nice interface to be able to view all of the backend information and updated if you have the correct permissions.

## Table of Content for Tutorial

I have created docs for step-by-step creating django project.

![GIF of Docs](#)

1. __[Installation:](1-Installation.md)__ Packages Needed, Install Django.
2. __[Applications and Routes:](2-Applications-and-Routes.md)__ Blog App, First View, Map view to urls, Adding another routes.
3. __[Templates:](3-Templates.md)__
4. 

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
