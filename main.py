from pprint import pprint

def get_data(file_name):
    data = dict()
    with open(file_name) as file:
        for line in file:
            cookbook = line.strip()
            counter = int(file.readline())

            temp_list = []
            for item in range(counter):
                ingredient, quantity, measure = file.readline().split(' | ')
                temp_list.append(
                    {
                    'ingredient_name': ingredient,
                    'measure': measure,
                    'quantity': quantity
                    }
                )
            data[cookbook] = temp_list
            file.readline()
    return data
# pprint(get_data('recipes.txt'))

def get_shop_list_by_dishes(dishes, person_count):
    cooking_today = []
    cooking_today = get_data('recipes.txt')[dishes]

    for ingredients in cooking_today:

        print(f'{dishes}:')
        for product, measure, quantity in ingredients:
            quantity = int(quantity) * person_count
            print(f'{product} {quantity} {measure}')


get_shop_list_by_dishes('Запеченный картофель', 7)