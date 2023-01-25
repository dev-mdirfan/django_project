from django.shortcuts import render

''' 1. previous views

# importing response
# from django.http import HttpResponse

# Create our views here.

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')
'''

posts = [
    {
        'author': 'Mohd Irfan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 19, 2023'
    },
    {
        'author': 'Alita',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 20, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})