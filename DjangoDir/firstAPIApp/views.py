from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    content = "<html><body><h1>Welcome</h1></body></html>"
    # return render(request,content)
    return HttpResponse(content)