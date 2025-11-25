from django.urls import path
from . import views

urlpatterns = [
    # path('menu-items', views.MenuItemsView.as_view()), #(1)
    # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()), #(1)
    path('menu-items/', views.menu_items),  #(2), (3)
    path('menu-items/<int:id>', views.single_item), #(2),(3)
    path('category/<int:pk>', views.category_detail, name='category-detail'), #(3)
        #"name" is needed when using "HyperlinkRelatedField" in "serializers.py"
    path('menu/', views.menu),
    path('welcome/', views.welcome)
]













