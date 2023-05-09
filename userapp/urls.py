
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name="userapp"

urlpatterns = [
    path("index",UserIndex,name="index"),
    path("test",Test,name="test"),
    path('login', login_view, name='login'),
    path("signup",SignUp,name="signup"),
    path('logout/', LogoutView.as_view(next_page='../index'), name='logout'),
    path("postcontent",PostContent,name="postcontent"),
    path("viewall",ViewTopics,name="viewall"),

]