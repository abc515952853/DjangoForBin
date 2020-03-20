from django.shortcuts import render
from blog.models import *
from django.http import HttpResponse
import json


# Create your views here.


def index(request,*args,**kwargs):
    blog_index = Article.objects.values()
    # context = {
    #     'blog_index':blog_index,
    # }
    print(blog_index)
    # print(request.method)
    # print(json.loads(request.body))
    # print(request.POST)
    # print(request.GET)
    # print(request.user.is_authenticated)
    # # return render(request, 'index.html',context)
    return HttpResponse(blog_index)