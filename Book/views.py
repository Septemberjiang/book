from django.http import HttpResponse
from django.shortcuts import render,redirect
from Book import models
from Book.models import User


def log(request):
    if request.method =='GET':
        # class_name = request.POST.get('class_name')
        # models.Classes.objects.create(name=class_name)
        # return  redirect('/class_list/')
        return render(request,'home.html')
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')

def register(request):
    if request.method =='GET':
        return render(request,'register.html')

    if request.method == "POST":
        user_name = request.POST.get('text')
        print('user_name:',user_name)
        password = request.POST.get('password')
        print('password:',password)
        username = User.objects.filter(username=user_name)
        if username:
            return HttpResponse("用户名已存在。")
        user = User()
        user.username=user_name
        user.password=password
        user.save()

