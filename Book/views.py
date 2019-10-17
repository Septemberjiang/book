from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from Book import models
from Book.models import User
from django.views import View


class log(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        log_list = models.User.objects.filter(username=user_name)
        pwd = models.User.objects.filter(password=password)
        if log_list and pwd:
            return redirect('/bookhome/')
        else:
            err_msg = '用户名或密码错误'
        return render(request, 'home.html',{'err_msg':err_msg})


class BookHome(View):
    # @login_required
    def get(self,request):
        return render(request,'book_home.html')

class register(View):
    def get(self, request):
        print('0000')
        return render(request,'register.html')

    def post(self,request):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        username = User.objects.filter(username=user_name)
        if username:
            return HttpResponse("用户名已存在。")
        # models.User.objects.create(name=user_name)
        # models.User.objects.create()

        user = User()
        user.username=user_name
        user.password=password
        user.save()
        return render(request, 'home.html')


