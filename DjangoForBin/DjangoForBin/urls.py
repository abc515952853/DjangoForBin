"""DjangoForBin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# from django.conf.urls import url
# from . import view
# from DjangoForBin.view import hello
# from DjangoForBin.testdb import testdb

# urlpatterns = [
#     # path('hello/', admin.site.urls),
#     # url(r'^$', view.hello1),
#     url(r'^$', view.hello2),
# ]


# from django.conf.urls import *
from DjangoForBin import view
# from DjangoForBin.testdb import testdb
# from DjangoForBin import search,search2
from django.urls import path,include

# from django.conf.urls import url,include
from django.contrib import admin
from blog.views import  index


extra_patterns = [
    path('hello/', view.hello),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('^$', my_homepage_view),
    # path('hello/', view.hello),
    # url('^hello3/$', hello3),
    # url('^testdb/$', testdb),
    # url('^search-form/$', search.search_form),
    # url('^search/$', search.search),
    # url('^search-post/$', search2.search_post),
    # url('^time/$',current_datetime),
    # url('^currenttime/$',current_datetime),
    # url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    # path('articles/(\d{4})/(\d{2})/(\d{2})/',method_splitter),
    # # url(r'^somepage/$',method_splitter),
    # path('<month>/articles/<year>/',view.method_splitter),
    # path(r'somepage/',method_splitter, {'GET': 'views.some_page_get', 'POST': 'views.some_page_post','DELETE':'11111111'}),
    # path('<year>/hehehe/', include('TestModel.testurl.urlone'),{'aaa':'1111'}),
    # path('gagaga/',include(extra_patterns)),
    # path('post/',include('TestModel.testurl.urlone')),


    # path(r'bbb/', include("TestModel.testurl.urlone",namespace = 'bbb')),
    # path(r'ccc/', include("TestModel.testurl.urlone",namespace = 'ccc')),
    # path(r'ccc/',index),
    path(r'login/',view.login),
    path(r'event_manage/',view.event_manage),
    path(r'accounts/login/',view.login)
]




handler400 = view.bad_request
handler403 = view.permission_denied
handler404 = view.page_not_found
handler500 = view.page_error
