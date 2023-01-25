from django.urls import path

from . import views

urlpatterns = [
    # creating path for blog home page
    path('', views.home, name='blog-home'),
    # adding about route
    path('about/', views.about, name='blog-about'),
]