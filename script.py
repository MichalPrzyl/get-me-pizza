FILENAME = 'menu.txt'

I_DONT_WANT_INGREDIENTS = ['pieczarki',
                           'ananas',
                           'kukurydza',
                           'cebula',
                           'świeży szpinak']

def filter_pizzas(obj):
    ingredients = obj['ingredients'].split(', ')
    
    if any([x in ingredients for x in I_DONT_WANT_INGREDIENTS]):
        return False
    return True

def get_proper_obj_from_str(splitted_value: str):
    lines = splitted_value.split('\n')
    lines = [line for line in lines if line]
    assert len(lines) == 2, 'There should be 2 lines.'
    name = lines[0]
    ingredients = lines[1]
                                 
    output = {
        'name': name,
        'ingredients': ingredients
    }

    return output

with open(FILENAME, 'r') as file:
    content = file.read()
    elements = content.split('\n\n')

assert elements, "wrong content splitting"

options = []

for element in elements:
    menu_element = get_proper_obj_from_str(element)
    options.append(menu_element)

filtered_pizzas = list(filter(filter_pizzas, options))

filtered_pizzas_names = list(map(lambda el: el['name'], filtered_pizzas))

for pizza_name in filtered_pizzas_names:
    print(f"pizza_name: {pizza_name}")
