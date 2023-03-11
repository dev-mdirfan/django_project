# Templates

Learning templates in django - We can write entire HTML doctype document in the functions of the views. But we do that for every single views. Best way to do that using templates.

- [Templates](#templates)
  - [Creating templates](#creating-templates)
    - [Add dummy data in posts](#add-dummy-data-in-posts)
    - [Replacing home.html into ginger templates](#replacing-homehtml-into-ginger-templates)
    - [Creating Base.html](#creating-basehtml)
  - [Adding Bootstrap](#adding-bootstrap)
    - [Adding Navigation](#adding-navigation)


Within `blog` directory create a new directory named as `templates` this can be seen as `blog/templates/blog/`

## Creating templates

```shell
blog -> templates -> blog -> template.html
```

- create two files -

```shell
blog
|---templates
|     |----blog
|     |     |---home.html
|     |     |---about.html
```

- Write an HTML Doc in `home.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Blog Home!</h1>
</body>
</html>
```

- write in `about.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>About Page</h1>
</body>
</html>
```

- Now we have to add our blog application to our list of installed apps. It recommended to add configuration to our project's `setting.py`
- Our __app configuration__ is located inside our `app.py` module within our application.

Copy the class name from app.py and paste it in `settings.py` module of the project.

```py
INSTALLED_APPS = [
  'blog.apps.BlogConfig',
]
```

Now let's use the template that we have created so that it render that whenever we navigate to our home page. We have to point our blog views to use those templates.

```py
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')
```

### Add dummy data in posts

Let's create some post that has some dummy data. Open `blog/views.py`

```py
from django.shortcuts import render

posts = [
    {
        'author': 'MdIrfan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 11 2023',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 12 2023',
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
```

### Replacing home.html into ginger templates

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% for post in posts %}
        <h1>{{ post.title }}</h1>
        <p>By {{ post.author }} on {{ post.date_posted }}</p>
        <p> {{ post.content }} </p>
    {% endfor %}
</body>
</html>
```

```py
python manage.py runserver
```

2. Let's change the title with specific post of the `home.html` and `about.html`

```py
{% if title %}
        <title>Django Blog - {{ title }}</title>
{% else %}
        <title>Django Blog</title>
{% endif %}
```
- change in `blog/views.py`
```py
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
```

### Creating Base.html

Similar Repeating code. It would be better to have in single place whenever we change if change in all places. That is inheritance

1. Let's create a new file `base.html` inside `blog/templates/blog/base.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% if title %}
        <title>Django Blog - {{ title }}</title>
    {% else %}
        <title>Django Blog</title>
    {% endif %}
</head>
<body>
    {% block content %} {% endblock %}
</body>
</html>
```

2. Change in `home.html`

```h
{% extends "blog/base.html" %}
{% block content %}
    {% for post in posts %}
        <h1>{{ post.title }}</h1>
        <p>By {{ post.author }} on {{ post.date_posted }}</p>
        <p> {{ post.content }} </p>
    {% endfor %}
{% endblock content %}
```

3. Change in `about.html`

```h
{% extends "blog/base.html" %}
{% block content %}
    <h1>About Page</h1>
{% endblock content %}
```

## Adding Bootstrap

1. Change `base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    {% if title %}
        <title>Django Blog - {{ title }}</title>
    {% else %}
        <title>Django Blog</title>
    {% endif %}
</head>
<body>
    <div class="container">
        {% block content %} {% endblock %}
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

### Adding Navigation

