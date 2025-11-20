from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

### I'll just focus on fcn views, not class views


# Create your views here.
def first(request):
    # content = "<html><body><h1>Welcome</h1></body></html>"
    # content = "<h3>Hola</h3>"
    content = """
        <ul>
            <li> This is a list </li>
        </ul>
    """
    # return render(request,content)
    return HttpResponse(content)

@csrf_exempt
    #Needed when not doing POST with forms
def second(request):
    content = "<h1>Regular</h1>"
    if request.method == 'GET':
        content = "<h1>This is a GET</h1>"
    if request.method == 'POST':
        content = "<h1>This is a POST</h1>"
    
    return HttpResponse(content)

# class Third(View):
#     def get(self, request):
#         content = "'Third' GET"
#         return HttpResponse(content)
    
#     def post(self, request):
#         # {% csrf_token %}
#         content = """
#         # {% csrf_token %}]
#         <h1>'Third' POST</h1>
#         """
#         return HttpResponse(content)
    
# class PathParam(View):
#     def get(self, request, name, id):
#         content = f"<h1>Path get - Name: {name} and ID: {id}</h1>"
#         return HttpResponse(content)
    
#     @csrf_exempt
#     def post(self, request, name, id):
#         content = f"<h1>Uno: {name} and Dos: {id}</h1>"
#         # return HttpResponse(content)
#         return JsonResponse(content)
    
# class QueryParam(View):
#     def get(self, request):
#         name = request.GET['name']
#         id_ = request.GET['id']
#         content = f"<h1>Query get - Nombre: {name} y ID: {id_}</h1>"
#         return HttpResponse(content)
    
#     @csrf_exempt
#     def post(self, request):
#         name = request.POST['name']
#         id_ = request.POST['id']
#         content = f"<h1>Nom: {name} et ID: {id_}</h1>"
#         return HttpResponse(content)

def hello(request):
    template = loader.get_template('hello.html')
    context = {'name': 'Jose'}
    return HttpResponse(template.render(context, request))


def showform(request):
    template = loader.get_template("form.html")
    context = {}
        #An empty content {} is necessary
    return HttpResponse(template.render(context, request))

def getform(request):
    if request.method == "POST":
        id_ = request.POST['id']
        name = request.POST['name']
    template = loader.get_template('hello.html')
    context = {'name': name}
    return HttpResponse(template.render(context, request))

















