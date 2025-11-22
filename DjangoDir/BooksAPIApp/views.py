from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, QueryDict
from django.forms.models import model_to_dict
from django.template import loader
from .forms import BookDetails
from .models import Books

# Note: results of API are delivered in JSON
    # Thus use 'model_to_dict'
        # book = Book.objects.get(pk=16)
        # return JsonResponse(model_to_dict(book))

# Use "QueryDict" to access elements of JSON payload
    # requst_body = QueryDict(request.body)
    # title = request_body.get('title')

# Create your views here.
def home(request):
    if request.method == 'GET':
        content = "<h1>Homepage</h1>"
        return HttpResponse(content)
    else:
        content = 'Home: not a GET'
        return HttpResponse(content)
    
def initial_books(request):
    form = BookDetails()
    return render(request, "book_form.html", {"form": form})

def all_books(request):
    #Delivers all books in DB
    #GET Features:
        #List books that are available for purchase
        #List books that are out of stock
    #POST Features:
        # Create new book
            # Success => Status 201
            # Missing fields => status 400
    if request.method == 'GET':
        content = "<h1>all_books GET</h1>"
        return HttpResponse(content)
    if request.method == 'POST':
        content = "<h1>all_books POST</h1>"
        return HttpResponse(content)
    return


def one_book(request, pk):
    # Shows only a single book
    # GET Features:
        # If request book that no exists, give 404
        # Result is a sigle item, not a list
            # Thus, it should NOT be in a list bracket
    # PUT features:
        # Edit a single book
    # DELETE Features:
        # Delete a single book
    if request.method == 'GET':
        content = "<h1>one_books GET</h1>"
        return HttpResponse(content)
    if request.method == 'POST':
        content = "<h1>one_books POST</h1>"
        # # Steps:
        #     # 1. Createa a "Books" model/table
        #     # 2. Create a form for "CreateBook"
        #     # 3. Extract the details from the form
        #     # 4. Save the details to the model
        #     # 5. Return HTTP
        # # Step 1: Done beforehand
        # # Step 2: Create form
        # book = BookDetails(request.POST)
        # # Step 3: Extract details
        # book_id = request.POST['book_id']
        # title = request.POST['title']
        # author = request.POST['author']
        # price = request.POST['price']
        # inventory = request.POST['inventory']
        # # Step 4: Save book to DB
        # book.save()
        # # Step 5: return HTTP
        # template = loader.get_template("confirmed_creation.html")
        # context = {
        #     'book_id': book_id,
        #     'title': title,
        #     'author': author,
        #     'price': price,
        #     'inventory': inventory,
        # }
        return HttpResponse(content)
    if request.method == 'PUT':
        content = "<h1>one_books PUT</h1>"
        return HttpResponse(content)
    if request.method == 'DELETE':
        content = "<h1>one_books DELETE</h1>"
        return HttpResponse(content)
    return












