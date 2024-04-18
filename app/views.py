import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .serializer import RecipeSerializer
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

def recipe_search(ingredient):
    app_id = APP_ID
    app_key = APP_KEY
    
    url = 'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}%09&random=true'.format(
        ingredient, app_id, app_key
    )
    
    try:
        result = requests.get(url)
        result.raise_for_status()
        data = result.json()
        return data.get('hits', [])
    except requests.RequestException as e:

        return []

class FavouriteRecipeListView(APIView):
    def get(self, request):
        favourite_recipes = Recipe.objects.all()
        serializer = RecipeSerializer(favourite_recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RecipeSearchView(APIView):
    def get(self, request, query):
        
        results = recipe_search(query)
        
        sorted_results = sorted(results, key=lambda x: x['recipe']['calories'])
        
        serializer = RecipeSerializer([
            {
                'title': hit['recipe']['label'],
                'image': hit['recipe']['images']['REGULAR']['url'],
                'ingredients': hit['recipe']['ingredientLines'],
                'diet_labels': hit['recipe'].get('dietLabels', []),
                'health_labels': hit['recipe'].get('healthLabels', []),
                'cautions': hit['recipe'].get('cautions', []),
                'calories': hit['recipe']['calories'],
                'total_time': hit['recipe']['totalTime'],
                'meal_type': hit['recipe'].get('mealType', []),
                'yield_amount': hit['recipe']['yield'],
                'url': hit['recipe']['url']
            } 
            for hit in sorted_results  
        ], many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddFavouriteRecipeView(APIView):
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
