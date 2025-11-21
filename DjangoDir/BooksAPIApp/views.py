from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'GET':
        content = "<h1>Homepage</h1>"
        return HttpResponse(content)
    else:
        content = 'Home: not a GET'
        return HttpResponse(content)