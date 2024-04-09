from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'ingredients', 'diet_labels', 'health_labels', 'cautions', 'calories', 'meal_type', 'yield_amount', 'url']
