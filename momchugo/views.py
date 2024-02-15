"""
#02.15 01:38
from django.http import HttpResponse
def first_page(request):
    a='<h1>Hello Momchugo</h1>'
    return HttpResponse(a)
#02.15 01:38
"""

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')