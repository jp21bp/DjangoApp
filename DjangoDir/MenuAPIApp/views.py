from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItems, Category
from .serializers import MenuItemSerializer, CategorySerializer
from django.shortcuts import get_object_or_404



# # (1)Using generics-views w/ regular ModelSerializer
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItems.objects.all()
#     serializer_class = MenuItemSerializer

# class SingleMenuItemView(
#     generics.RetrieveUpdateAPIView,
#     generics.DestroyAPIView
# ):
#     queryset = MenuItems.objects.all()
#     serializer_class = MenuItemSerializer





# (2)Using fcn-views w/ regular Serializer
# (3) Also works with custom "ModelSErializer"
@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET':
        # items = MenuItems.objects.all()
        items = MenuItems.objects.select_related('category').all()
            #"select_related" details:
                # Used when retrieveing multiple instances
                # Used when converting a connected model to string
                # Loads the RELATED model in a SINGLE SQL code
                # Makes API MORE EFFICIENT
                    # Ensure that only ONE sql query is called for
                            #every item to load relative data
                    # Instead of running SEPARATE SQL queries 
                            #for separate items
        # serialized_item = MenuItemSerializer(items, many=True)
            #"many=True" needed when applying serializer to many instances
        serialized_item = MenuItemSerializer(
            items,
            many=True,
            context={'request': request},
                #Needed when using "HyperlinkRelatedField" in 'seralizers.py'
        )
        return Response(serialized_item.data)
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
            #"request.data" = client's input data; request payload
        serialized_item.is_valid(raise_exception=True)
            # Data validation
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_200_OK)

@api_view()
def single_item(request, id):
    # item = MenuItems.objects.get(pk=id)
    item = get_object_or_404(MenuItems, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)


@api_view()
def category_detail(request, pk):
    # View for details of a SINGLE category instance
    category = get_object_or_404(Category, pk=pk)
    serialzed_category = CategorySerializer(category)
    return Response(serialzed_category.data)








