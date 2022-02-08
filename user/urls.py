from django.contrib.auth import views
from django.urls import path
from . import views

urlpatterns = [path('login/',views.login),
               path('post/',views.userPost)
               ]