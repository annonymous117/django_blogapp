from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from django.conf import settings
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from.forms import *
# Create your views here.
def UserIndex(request):
    data={}
    return render(request,"base.html",data)

def Test(request):
    return HttpResponse('welcome home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/userapp/index')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'registration/login.html')

def SignUp(request):
    #return HttpResponse(request.method)
    myform=UserCreationForm(request.POST or None)
    data={"form":myform,"title":"User Registration"}
    if (request.method=="POST"):
        if myform.is_valid():
            user=myform.save()
            login(request,user)
            # messages.success(request,"welcome you are logged in")
            return redirect('/userapp/login_view')
            
    return render(request,"registration/register.html",data)
def PostContent(request):

    username=request.user

    form =PostContentForm(initial={"author":username})
    if request.method=="POST":
        form=PostContentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/userapp/viewall")
    data={"pagetitle":"Available Topics","forms":form}
    return render(request,'post_content.html',data)

def ViewTopics(request):
    from .models import PostContent
    content=PostContent.objects.all()
    data={"pagetitle":"All Available Topics ","content":content}
    return render(request,'main.html',data)