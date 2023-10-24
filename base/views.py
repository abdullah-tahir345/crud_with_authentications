from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import RegStu

@login_required(login_url='login')
def HomePage(request):
    student_data = RegStu.objects.all()
    context = {'student_data':student_data}
    return render(request, 'base/home.html', context)

def AddStudentPage(request):
    
    if request.method == "POST":
        name = request.POST['name']
        roll = request.POST['roll']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        
        student = RegStu()
        student.name = name
        student.roll = roll
        student.phone = phone
        student.email = email
        student.address = address
        
        student.save()
        return redirect('home')
        
    
    context = {}
    return render(request, 'base/add_student.html', context)

def DeleteStudent(request, std_id):
    std = RegStu.objects.get(pk=std_id)
    std.delete()
    return redirect('home')

def UpdateStudent(request, std_id):
    std = RegStu.objects.get(pk=std_id)
    context = {'std':std}
    return render(request, 'base/update_student.html', context)

def DoUpdateStudent(request, std_id):
    if request.method == "POST":
        name = request.POST['name']
        roll = request.POST['roll']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        
        student = RegStu.objects.get(pk=std_id)
        student.name = name
        student.roll = roll
        student.phone = phone
        student.email = email
        student.address = address
        
        student.save()
        return redirect('home')
        
    return render(request, 'base/update_student.html', context)

def SignupPage(request):
    
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        if pass1 != pass2:
            messages.error(request, "Passwords doesn't match")
            return redirect('signup')
        else:    
            user = User.objects.create_user(username, email, pass1)
            user.save()
            return redirect('login')
    
    context = {}
    return render(request, 'base/signup.html', context)

def LoginPage(request):
    
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password1']
        
        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials!!!")
            return redirect('login')
        
    context = {}
    return render(request, 'base/login.html', context)

def LogoutPage(request):
    logout(request)
    messages.info(request, "Logout Successfully!!!")
    return redirect('login')