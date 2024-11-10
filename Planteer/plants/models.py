from django.db import models
from django.utils.timezone import now

class Plant(models.Model):
    class Category(models.TextChoices):
        VEGETABLE = 'vegetable', 'Vegetable'
        FRUIT = 'fruit', 'Fruit'
        HERB = 'herb', 'Herb'
        FLOWER = 'flower', 'Flower'
        CACTI = 'cacti', 'Cacti'
        DESERT = 'desert', 'Desert'
        
        
    
    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    category = models.CharField(choices=Category.choices, max_length=20)    
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    

