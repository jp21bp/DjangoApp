from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first),
    path('second/', views.second),
    # path('third/', views.Third.as_view()),
    # path('path-param/<name>/<id>', views.PathParam.as_view()),
    #     #EX: http://127.0.0.1:8000/path-param/jose/24
    # path('query-param/', views.QueryParam.as_view()),
    #     #EX: http://127.0.0.1:8000/query-param?name=jose&id=1
    path('hello-template/', views.hello),
    path('show-form/', views.showform),
    path('show-form/getform', views.getform),
]