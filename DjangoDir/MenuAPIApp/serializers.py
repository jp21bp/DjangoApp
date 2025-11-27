from rest_framework import serializers
from .models import MenuItems, Category
from decimal import Decimal
import bleach

# # (1) Regular "ModelSerializer"
# class MenuItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuItems
#         fields = ['id', 'title', 'price']
#             #Will only display 'id', 'title', and 'price'


# # (2) Regular "Serializer"
# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


# (3) Custom "ModelSeraializer" for "Category"
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

# (3) Custom "ModelSerializer" for "MenuItems"
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
        #Changes the name of the field
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
        #Turns a fcn into a field
    # category = serializers.StringRelatedField() # Shows STRING represenation
        #Gets the "__str__" for the corresponding field
            #By defaults, its usually "<Field> object (pk)"
            # THis can be changed by overriding "__str__" in 
                    #corresponding model
    category = CategorySerializer(read_only=True) #Shows JSON representation
    category_id = serializers.IntegerField(write_only=True)
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(),
    #     view_name='category-detail',
    # )
    def calculate_tax(self, product:MenuItems):
        return product.price * Decimal(1.1)

    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])
        if(attrs['price'] < 2):
            raise serializers.ValidationError('price > 2')
        if(attrs['inventory'] < 0):
            raise serializers.ValidationError('inventory < 0')
        return super().validate(attrs)

    class Meta:
        model = MenuItems
        fields = ['id', 'title', 'price', 'stock', \
                  'price_after_tax', 'category', 'category_id']

    






