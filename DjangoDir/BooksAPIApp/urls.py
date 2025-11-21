from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('books/', views.all_books),
    path('books/<bookId>', views.one_book),
]