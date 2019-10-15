from django.http import HttpResponse
from django.shortcuts import render,redirect
from Book import models
from Book.models import User
from django.views import View

class log(View):
    def get(self,request):
        # class_name = request.POST.get('class_name')
        # models.Classes.objects.create(name=class_name)
        # return  redirect('/class_list/')
        return render(request,'home.html')
    def post(self,request):
        user_name = request.data.get('username')
        password = request.data.get('password')

class register(View):
    def get(self, request):
        return render(request,'register.html')

    def post(self,request):
        print('---->',request)
        user_name = request.POST.get('username')
        print('user_name:',user_name)
        password = request.POST.get('password')
        print('password:',password)
        username = User.objects.filter(username=user_name)
        if username:
            return HttpResponse("用户名已存在。")
        # user = User()
        # user.username=user_name
        # user.password=password
        # user.save()

