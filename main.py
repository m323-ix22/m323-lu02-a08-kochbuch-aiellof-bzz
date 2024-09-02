"""
Created on Fri Mar 12 14:
"""
import json


# Funktion zum Laden eines Rezepts aus einem JSON-String
def load_recipe(json_str):
    return json.loads(json_str)


# Funktion zur Anpassung der Rezeptmengen für eine variable Personenanzahl
def adjust_recipe(recipe_data, servings):
    factor = servings / recipe_data['servings']
    adjusted_ingredients = {
        ingredient: amount * factor
        for ingredient, amount in recipe_data['ingredients'].items()
    }
    # Neues angepasstes Rezept zurückgeben, ohne das Original zu verändern
    return {
        'title': recipe_data['title'],
        'ingredients': adjusted_ingredients,
        'servings': servings
    }


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts als JSON-String
    recipe_json = (
        '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, '
        '"Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    )

    # Rezept aus JSON laden
    original_recipe = load_recipe(recipe_json)

    # Neue Anzahl an Personen
    new_serving_size = 2

    # Rezept für neue Anzahl an Personen anpassen
    adjusted_recipe = adjust_recipe(original_recipe, new_serving_size)

    # Angepasstes Rezept anzeigen
    print('Originales Rezept:', original_recipe)
    print('\nAngepasstes Rezept:', adjusted_recipe)
