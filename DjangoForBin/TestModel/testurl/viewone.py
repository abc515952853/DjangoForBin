from django.http import HttpResponse
from django.urls import reverse

def xixixi(request,*args,**kwargs):
    print(args) 
    print(kwargs)
    print(request.GET.get('abc',None))
    return HttpResponse("Hello xixixi! ")

def hello(request,*args,**kwargs):
    print('1')
    return HttpResponse("Hello!")


def aaa(request):
    print(request.resolver_match.namespace)
    return HttpResponse(reverse("app02:index",current_app=request.resolver_match.namespace))
    # return HttpResponse('11')