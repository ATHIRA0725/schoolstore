from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from . models import Formtable


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,"invalid user")
            return redirect('login')

    return render(request,'login.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return render(request,'register.html')
        elif password != cpassword:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        return render(request, 'register.html')


def newpage(request):
    return render(request,'newpage.html')

def form(request):
     # if request.method == 'POST':
     #     username=request.POST['username']
     #     dob=request.POST['dob']
     #     age=request.POST['age']
     #     mailid=request.POST['mailid']
     #     mobile=request.POST['mobile']
     #     adrs=request.POST['adrs']
     #     gender=request.POST['gender']
     return render(request,'form.html')


def logout(request):
    return render(request,'index.html')