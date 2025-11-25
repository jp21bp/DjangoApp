from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from .models import MenuItems, Category
from .serializers import MenuItemSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
from rest_framework_csv.renderers import CSVRenderer
from rest_framework_yaml.renderers import YAMLRenderer


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
        
        #Implementing Filtering
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(price__endswith=search)
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

@api_view()
@renderer_classes([TemplateHTMLRenderer])
# @renderer_classes([CSVRenderer])
# @renderer_classes([YAMLRenderer])
def menu(request):
    items = MenuItems.objects.select_related('category').all()
        #Recall: "select_related" = for efficiency
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data': serialized_item.data}, template_name='menu-items.html')

@api_view()
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = '<html><body><h1>Welcome</h1></body></html>'
    return Response(data)


