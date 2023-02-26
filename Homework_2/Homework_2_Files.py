from pprint import pprint

def read_recepies(file):
    with open(file, 'rt', encoding='utf-8') as file:
        dishes_available = {}
        for line in file:
            dish_name = line.strip()
            ingredients_amount = int(file.readline())
            ingredients = []
            for _ in range(ingredients_amount):
                ingredient = file.readline().strip()
                ingredient_name, amount, unit = ingredient.split(' | ')
                ingredients.append(
                    {'Ингредиент': ingredient_name,
                    'Количество': amount,
                    'Мера': unit,}
                )
            dishes_available[dish_name] = ingredients
            file.readline()
    return dishes_available

# pprint(read_recepies('recipes.txt'), sort_dicts = False)

pprint(read_recepies('recipes.txt'), sort_dicts=False)