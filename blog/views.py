from django.shortcuts import render
from .models import Post
''' 1. previous views

# importing response
# from django.http import HttpResponse

# Create our views here.

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')
'''

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})