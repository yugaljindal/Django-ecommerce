from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE,default=3)
    description = models.CharField(max_length = 200,default= '')
    image = models.ImageField(upload_to='upload/Product/',default='')

    def __str__(self):
        return self.name + ' --- ' + str(self.category)
 
