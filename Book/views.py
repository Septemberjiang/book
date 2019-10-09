from django.shortcuts import render,redirect
from Book import models

def log(request):
    if request.method =='GET':
        # class_name = request.POST.get('class_name')
        # models.Classes.objects.create(name=class_name)
        # return  redirect('/class_list/')
        return render(request,'home.html')
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        print("1111")

def register(request):
    if request.method =='GET':
        # class_name = request.POST.get('class_name')
        # models.Classes.objects.create(name=class_name)
        # return  redirect('/class_list/')
        return render(request,'home.html')

    if request.method == "POST":
        print(111)