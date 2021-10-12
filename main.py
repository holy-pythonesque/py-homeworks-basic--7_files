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
                     'quantity': quantity,
                     'measure': measure
                     }
                )
            data[cookbook] = temp_list
            file.readline()
    return data
pprint(get_data('recipes.txt'))

def get_shop_list_by_dishes(dishes, person_count):
    cookbook = get_data('recipes.txt')
    for dish in cookbook:
        if dish == dishes:
            new_quantity = person_count * cookbook[dishes['quantity']]
        ...