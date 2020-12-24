input_file = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\21dec_input.txt","r")

input_lines = input_file.readlines()

foods = []

for a_line in input_lines:
    line_split = a_line.split(" (")
    allergy_warnings = line_split[1]
    ingredients = line_split[0]
    
    allergy_warnings = allergy_warnings.replace(")", "")
    allergy_warnings = allergy_warnings.replace("\n", "")
    allergy_warnings = allergy_warnings.replace("contains ", "")
    allergy_warnings = allergy_warnings.split(", ")

    ingredients = ingredients.split(" ")
    #print(ingredients)

    foods.append([ingredients, allergy_warnings])

#print(foods)

#create list of possible ingredients for allergin
possible_allergens = {}
for a_food in foods:
    for an_allergen in a_food[1]:
        if an_allergen not in possible_allergens:
            possible_allergens[an_allergen] = a_food[0]
        else:
            for an_ingredient in a_food[0]:
                if an_ingredient not in possible_allergens[an_allergen]:
                    possible_allergens[an_allergen].append(an_ingredient)

print(possible_allergens)
        


all_ingredients = []
confirmed_allergens = []
confirmed_non_allergens = []

