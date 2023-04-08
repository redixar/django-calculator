from django.http import HttpResponse
from django.shortcuts import render
 


def hello(request):
    return HttpResponse("Hello, World!")
 

def redixtar(request):
    return render(request, 'redixtar.html')
