from django.urls import path,include
from TestModel.testurl import viewone
from django.urls import re_path


app_name = "app02"

urlpatterns = [
    # re_path(r'^blog/(page-(\d+)/)?$', viewone.xixixi,{'bbb':'222',}),
    # path('hello',viewone.hello),

    path('aaa/', viewone.aaa, name="index"),
]