#coding:utf-8
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json
def index(request):
    return HttpResponse('welcome mysite')

def home(request):
    #return render(request,'index.html')
    #string = 'django 还是不错的'
    alist = ['html','css','javascript']
    bdict = {'name':'zhangsan','age':'18','sex':'man'}
    nums = map(str,range(100))
    jsonList = ['a','b']
    jsonList = json.dumps(jsonList)
    return render(request,'index.html',{'jsonList':jsonList,'nums':nums,'alist':alist,'bdict':bdict})


def home2(request):
    aList = ['mac','windows','linux']
    bdict = {'name':'zhangsan','age':19}
    nums = map(str,range(100))
    jsonList = ['a','b']

    return render(request,'index2.html',{'aList':aList,'bDict':bdict,'jsonList':jsonList,'nums':nums})

