# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def add(request):
    #get the params
    a = request.GET['a']
    b = request.GET['b']
    #calc
    c = int(a)+int(b)
    return HttpResponse(str(c)) 

def add2(request,a,b):
    c =int(a)+int(b)
    return HttpResponse(str(c))
    #return render(str(c))
