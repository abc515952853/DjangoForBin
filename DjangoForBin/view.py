from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
     return HttpResponse("Hello world ! ")

def hello1(request):
 return HttpResponse("Hello world ! ")

def hello2(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request,'hello.html',context)







 #python manage.py runserver 0.0.0.0:8000