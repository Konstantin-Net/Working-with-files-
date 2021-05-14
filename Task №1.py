from pprint import pprint

cook_book = {}
way = "C:\\Users\\Krasny\\PycharmProjects\\ Hello\\Netology\\Opening and reading a file, writing to a file\\"
with open(f"{way}recipes.txt", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if len(line) != 1 and "|" not in line and line != '':
            cook_book[line] = []
            dish = line
        elif "|" in line:
            ingredients = [i for i in line.split(" | ")]
            cook_book[dish].append({'ingredient_name': ingredients[0],
                                    'quantity': ingredients[1],
                                    'measure': ingredients[2]})

pprint(cook_book)
