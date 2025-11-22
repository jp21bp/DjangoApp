from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('', views.initial_books),
    path('books/', views.all_books),
    path('books/<pk>', views.one_book),
]