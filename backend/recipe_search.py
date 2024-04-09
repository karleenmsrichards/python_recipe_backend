import requests

def recipe_search(ingredient):
    app_id = '231a4088'
    app_key = '11a10b8d1263cde9136c121d17144f2c'
    
    result = requests.get(
        'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}%09&random=true'.format(
            ingredient, app_id, app_key
        )
    )
    
    data = result.json()
    
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')
    
    results = recipe_search(ingredient)
    
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print(recipe['url'])
        print(recipe['dietLabels'])
        print(recipe['healthLabels'])
        print(recipe['cautions'])
        print(recipe['ingredientLines'])
        print(recipe['calories'])
        print(recipe['totalTime'])
        print(recipe['yield'])
        print(recipe['mealType'])
        thumbnail_url = recipe['images']['THUMBNAIL']['url']
        print(thumbnail_url)

run()
