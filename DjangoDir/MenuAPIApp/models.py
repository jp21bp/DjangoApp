from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
        #Used for URLs naming
    title = models.CharField(max_length=255)

    #Overriding the string representation of the model
    def __str__(self)->str:
        return self.title

class MenuItems(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
        #This comes off as a "CharField", not an int/float
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        default=1
    )

    #Overriding str representation of model
    def __str__(self)->str:
        return self.title
