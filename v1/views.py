from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("Hi, you're trying to login.")

def dumbdumb(request):
    return HttpResponse("Nothing to see here dumb dumb")