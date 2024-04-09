from django.db import models

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    image = models.URLField(max_length=2000) 
    ingredients = models.TextField()  
    diet_labels = models.CharField(max_length=500, blank=True, null=True) 
    health_labels = models.CharField(max_length=500, blank=True, null=True) 
    cautions = models.CharField(max_length=200, blank=True, null=True) 
    calories = models.FloatField(blank=True, null=True) 
    meal_type = models.CharField(max_length=100, blank=True, null=True)
    yield_amount = models.IntegerField(blank=True, null=True) 
    url = models.URLField(max_length=500) 

    def __str__(self):
        return self.title
