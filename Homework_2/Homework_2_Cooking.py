from pprint import pprint

class Purchaser:
    def __init__(self, recipe_list):
       self.recipe_list = recipe_list

    def read_recipe_list(self):
       with open(self.recipe_list, 'rt', encoding='utf-8') as recipe_list:
        dishes_available = {}
        for line in recipe_list:
            dish_name = line.strip()
            ingredients_amount = int(recipe_list.readline())
            ingredients = []
            for _ in range(ingredients_amount):
                ingredient = recipe_list.readline().strip()
                ingredient_name, amount, unit = ingredient.split(' | ')
                ingredients.append(
                    {'Ингредиент': ingredient_name,
                    'Количество': int(amount),
                    'Мера': unit,}
                )
            dishes_available[dish_name] = ingredients
            recipe_list.readline()
        return dishes_available 

    def get_shop_list_by_dishes(self, dishes, person_amount):
        shop_list = {}
        incredients_to_buy = []
        for dish in dishes:
            if dish in self.read_recipe_list():
                for element in self.read_recipe_list()[dish]:
                    if element['Ингредиент'] in shop_list:
                        shop_list[element['Ингредиент']]['Количество'] += element['Количество'] * person_amount
                    else:
                        shop_list[element['Ингредиент']] = {
                        'Мера': element['Мера'],
                        'Количество': element['Количество'] * person_amount}
        return shop_list
                  

someone = Purchaser('recipes.txt')
#pprint(someone.read_recipe_list())
pprint(someone.get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3), sort_dicts=False)