"""
Created on Fri Mar 12 14:
"""
import json

# Funktion zum Laden eines Rezepts aus einem JSON-String
def load_recipe(json_string):
    return json.loads(json_string)

# Funktion zur Anpassung der Rezeptmengen für eine variable Personenanzahl
def adjust_recipe(recipe, new_servings):
    factor = new_servings / recipe['servings']
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipe['ingredients'].items()}
    # Neues angepasstes Rezept zurückgeben, ohne das Original zu verändern
    return {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': new_servings
    }


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts als JSON-String
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    # Rezept aus JSON laden
    recipe = load_recipe(recipe_json)

    # Neue Anzahl an Personen
    new_servings = 2

    # Rezept für neue Anzahl an Personen anpassen
    adjusted_recipe = adjust_recipe(recipe, new_servings)

    # Angepasstes Rezept anzeigen
    print("Originales Rezept:", recipe)
    print("\nAngepasstes Rezept:", adjusted_recipe)
