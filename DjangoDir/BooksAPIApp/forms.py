from django.forms import ModelForm
from BooksAPIApp.models import Books
from django import forms

class BookDetails(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
    # Making "book_id" required
    # book_id = forms.IntegerField(required=True)