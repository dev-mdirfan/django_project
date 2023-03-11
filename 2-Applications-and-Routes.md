# Applications and Routs

In this, we will be adding a blog application to site and also setting up some url routs so that we can start direct people to that he would like them to see. Let's get started.

- [Applications and Routs](#applications-and-routs)
  - [Creating blog app](#creating-blog-app)
    - [Write first view](#write-first-view)
    - [Mapping views to URLS](#mapping-views-to-urls)
    - [Map url to urls of main project directory](#map-url-to-urls-of-main-project-directory)
    - [Add another route](#add-another-route)


## Creating blog app

First lets create a __blog app__ for our site. The thinking behind the django here, is that you have the website project which we already created within that website you can have multiple apps for example we can have a blog section of our website that will be an app. And we can also have __store app__ section of the website.

- A single project can contain multiple apps like blog app, store app.

We will see in letter, that good thing for separating out different parts of the project. And another thing we can add single apps to multiple projects.

__Creating blog app:__

Stay on project directory in the same directory where `manage.py` file.

```py
python manage.py startapp blog
```

- Lets see the layout of the file structure -

```shell
tree
```

```shell
--- blog
|   |--- __init__.py
|   |--- admin.py
|   |--- apps.py
|   |--- migrations
|   |       |--- __init__.py
|   |--- models.py
|   |--- tests.py
|   |--- views.py
|--- db.sqlite3
|--- django_project
|       |--- __init__.py
|       |--- settings.py
|       |--- urls.py
|       |--- wsgi.py
|--- manage.py
```

### Write first view

You can see we already have imported __render__ we use that letter. But for now we also going to import `HttpResponse` from `django.http`.

__Write in `blog/views.py`:__

```py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
```

- here we are not using `request` we need to put on the parameter of the functions of the view.
- This is the logic how we want to handle when a user goes for __blog home page__. But, we have't actually mapped a urls patterns to this views function just yet.

### Mapping views to URLS

Now, we need to map the url in `/blog`. In that file where we map the url correspond to each view functions

To do that create a new file `urls.py` within `/blog` directory and write - (`/blog/urls.py`)

- Now this urls module is going to very similar to the urls modules that we saw in the `blog_project` directory.

```py
from django.urls import path
from . import views
# . is represents the current directory

urlpatterns = [
    # creating path for blog home page
    path('', views.home, name='blog-home'),
]

```

- They have `import path` here ans then they have list of `urlpatterns` that are using that paths.
- `views.home` (home) is the same name as we create function in views. - Home page route
- name parameter of the path is the `blog-home`. You might be wondering why I put the name as `blog-home` instead of just home that's because there will be time that we want to do a reverse lookup on this route and naming this something as generic as home could collide with other app route. If I had a store app then may be have an app that has home route also so I want to clear with the actual naming of this path.

### Map url to urls of main project directory
- Now, we have the url path for our blog home page map to our home function in the views file but this still would't work quite yet, because if you remember we have a urls module in main project directory also and that urls module will tell our whole website which urls should send us to our blog app. That might be confusing but lets this pull this up.

Open __project's__ `urls.py` file. Like we have seen before we already have one route of this admin that gets mapped to the admin site urls.

- We need to `import include` from `django.urls`. Now we can add list of patterns specify which route should go to blog urls.

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

- We latter use __Regular Expression__ to match their paths. And RE can be more complicated when routes going to pretty simple. Now run the server.
```py
python manage.py runserver
```

- It try to match the urls `admin/` or `blog/`. If you navigate to `/blog`, you can see text __Blog Home__. Now you open __View Page Source__, you seen only h1 tag written blog home text which we have returned.

### Add another route

- Add Function in `views.py`:

```py
def about(request):
    return HttpResponse('<h1>Blog About</h1>')
```

- Now map the this views function to urls of the blog. (means add another path to urlpatterns)

```py
path('about/', views.about, name='blog-about'),
```