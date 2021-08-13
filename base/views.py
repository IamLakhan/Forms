from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def form_general(request):
    return HttpResponse('Hello')

def greet(request):
    return HttpResponse('Hello {0}'.format(request.user))