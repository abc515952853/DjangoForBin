from django.http import HttpResponse,Http404
from django.shortcuts import render

import datetime


def hello(request):
    return HttpResponse("Hello world ! ")

def hello1(request):
 return HttpResponse("Hello world ! ")

def hello2(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request,'hello.html',context)

def my_homepage_view(request):
     return HttpResponse('页面不存在')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def  hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In {} hour(s), it will be {}.</body></html>".format(offset, dt)
    return HttpResponse(html)







 #python manage.py runserver 0.0.0.0:8000