
 
bags_containing_shiny_gold = ["shiny gold bags"]

# part 1, rules array no longer works like this
"""done_adding = False
while not done_adding:
    start_count = len(bags_containing_shiny_gold)
    for rule in rules:
        for bag_type in bags_containing_shiny_gold:
            if rule[0] not in bags_containing_shiny_gold:
                if bag_type[:-1] in rule[1]:
                    bags_containing_shiny_gold.append(rule[0])
    end_count = len(bags_containing_shiny_gold)
    done_adding = start_count == end_count
    
               

print(len(bags_containing_shiny_gold) - 1)"""

# part 2, rules array changed from part on 
rules_raw = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\7dec_input.txt","r")
rules_array = []
for rule_line in rules_raw:
    rule_line = rule_line.split(' contain ')
    #print(rule_line)
    if ", " in rule_line[1]:
        rule_line[1] = rule_line[1].split(", ")
    else:
        rule_line[1] = [rule_line[1]]
    rules_array.append(rule_line)
print(rules_array)


    
