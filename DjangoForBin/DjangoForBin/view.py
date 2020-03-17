from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render

from django.template import loader, Context,RequestContext


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


def  day_archive(request,year,month,day):
    date = datetime.date(int(year), int(month), int(day))
    print(date)
    html = "<html><body>{}年{}月{}日</body></html>".format(year,month,day)
    return HttpResponse(html)

def some_page(request):
    if request.method == 'GET':
        return HttpResponse('GET')
        # return GET(request)
    elif request.method == 'POST':
        return HttpResponse('POST')
        # return POST(request)
    raise Http404


##-------------------------------------------------------------------------------
def method_splitter(request,*args,**kwargs):
    # get_view = kwargs.pop('GET', None)
    # post_view = kwargs.pop('POST',None)
    # delete_view = kwargs.pop('DELETE',None)
    getUserName = request.GET.get('c',None)
    
    print(args) 
    print(kwargs)
    # print(args,kwargs,getUserName) 
    return HttpResponse(request.method)

def some_page_get(request):
    assert request.method == 'GET'
    return HttpResponse('Get')
def some_page_post(request):
    assert request.method == 'POST'
    return HttpResponse('Post')
##-------------------------------------------------------------------------------
def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }

def hello3(request):
    # t = loader.get_template('hello.html')
    # c = {'hello': 'Hello World!'}
    # html = t.render(c)
    # return HttpResponse(html)

    # context = {}
    # context['hello'] = 'Hello World!'
    # return render(request,'hello.html',context)
    return render(request,'hello.html',{'hello': 'I am view 1.'})





 #python manage.py runserver 0.0.0.0:8000

def page_not_found(request,exception):
    context = {}
    context['hello'] = 'Hello 404!'
    return render(request,'hello.html',context)

def page_error(request):
    context = {}
    context['hello'] = 'Hello 500!'
    return render(request,'hello.html',context)

def permission_denied(request,exception):
    context = {}
    context['hello'] = 'Hello 403!'
    return render(request,'hello.html',context)

def bad_request(request,exception):
    context = {}
    context['hello'] = 'Hello 400!'
    return render(request,'hello.html',context)
