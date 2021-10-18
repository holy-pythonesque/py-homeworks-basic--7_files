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
    cookbook = get_data('recipes.txt')
    # cooking_today = []
    for dish in dishes:
        print(f'{dish}:')
        for ingredients in cookbook[dish]:
            for items in ingredients:
                product, measure, quantity = ingredients.values()
            print(f'{product} {int(quantity)*person_count} {measure}')


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 7)


        # for ingredients in cooking_today:
        #     # print(ingredients) # ingredients = словарь целиком
        #     product, measure, quantity = ingredients.values()
        #     print(f' {product} {int(quantity) * person_count} {measure}')
        #     # quantity = int(quantity) * person_count
        #     # print(f'{product} {quantity} {measure}')


# псевдокод
# def new_function(dishes, person_count):
#     result = []
#     if result[product] != null:
#         result[product].quantity += quantity*person_count
#     else:
#         result[product] = {quantity: quantity*person_count, measure: measure}
'''задаёшь результирующий словарь, итерируешься по всем блюдам, 
для каждого блюда проходишь по ингредиентам. если очередной продукт 
из ингредиентов уже есть у нас в словаре, мы увеличиваем его количество 
на требуемое для текущего блюда; если нет - добавляем в словарь. 
в конце функции - возвращаем словарь result'''