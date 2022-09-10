def readfile(input,output):
    with open(input) as f:
        for line in f:
            output.append(line.strip())

def parse(source_data,cook_book):
    i = 0
    while i < len(source_data):
        if i == 0:
            dish = source_data[i]
        if i > 0: 
            if source_data[i-1] == '':
                dish = source_data[i]
        if dish:
            ingr_num = int(source_data[i+1])
            ingredients = []
            for ing in range(i+2,i+2+ingr_num):
                ing_dict = {}
                name,qt,measure = source_data[ing].split(' | ')
                ing_dict['quantity'] = qt
                ing_dict['ingredient_name'] = name
                ing_dict['measure'] = measure
                ingredients.append(ing_dict)
            cook_book[dish] = ingredients
        dish = 0
        i +=1

def get_shop_list_by_dishes(dishes,person_count,cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list.keys():
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],'quantity': int(ingredient['quantity']) * person_count}
            else:
                ing = ingredient['ingredient_name']
                amount_ing = shop_list[ing]['quantity']
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],'quantity': int(ingredient['quantity']) * person_count + amount_ing}    
    return shop_list


source_data = []
cook_book = {}
readfile('/home/alex/Python/python/Hello World/Files/recipes.txt',source_data)
parse(source_data,cook_book)
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 4, cook_book))
