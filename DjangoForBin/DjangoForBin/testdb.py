# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
  # response = ""
  # response1 = ""
  # test1 = Test(name='w3cschool.cn')
  # test1.save()
  # return HttpResponse("<p>数据添加成功！</p>")

  # list = Test.objects.all()
  # for var in list:
  #   response1 += var.name + " "
  # response = response1
  # return HttpResponse("<p>" + response + "</p>")

  Test.objects.filter(id=1).update(name='Cschool教程')
  Test.objects.all().delete()

  return HttpResponse("<p>" + '修改成功' + "</p>")

