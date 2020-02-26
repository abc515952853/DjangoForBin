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


from django.conf.urls import *
from DjangoForBin.view import hello
from DjangoForBin.testdb import testdb

urlpatterns = [
    url('^hello/$', hello),
    url('^testdb/$', testdb),
]
