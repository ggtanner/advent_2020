rules = {
'departure location': [50,692,705,969],
'departure station': [35,540 , 556,965],
'departure platform': [27,776 , 790,974],
'departure track': [48,903 , 911,955],
'departure date': [33,814 , 836,953],
'departure time': [34,403 , 421,966],
'arrival location': [37,489 , 510,963],
'arrival station': [46,128 , 150,960],
'arrival platform': [45,75 , 97,959],
'arrival track': [28,535 , 541,952],
'class': [38,340 , 349,966],
'duration': [42,308 , 316,969],
'price': [49,324 , 340,970],
'route': [31,627 , 648,952],
'row': [38,878 , 893,955],
'seat': [39,54 , 71,967],
'train': [36,597 , 615,960],
'type': [41,438 , 453,959],
'wagon': [42,370 , 389,971],
'zone': [36,114 , 127,965],
}

my_ticket = [107,157,197,181,71,113,179,109,97,163,73,53,101,193,173,151,167,191,127,103]

nearby_tickets_input = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\16_dec_nearby_tickets.txt","r")
nearby_tickets_raw = nearby_tickets_input.readlines()
nearby_tickets = []
for line in nearby_tickets_raw:
    line_filtered = []
    line = line.split(',')
    for item in line:
        item = int(item)
        line_filtered.append(item)
    nearby_tickets.append(line_filtered)

valid_tickets = []
ticket_error_rate = 0

for a_ticket in nearby_tickets:
    ticket_checks = []
    for a_field in a_ticket:
        field_checks = []
        for a_rule in rules:
            this_check = ((a_field >= rules[a_rule][0]) and (a_field <= rules[a_rule][1])) or ((a_field >= rules[a_rule][2]) and (a_field <= rules[a_rule][3]))
            field_checks.append(this_check)
        if not any(field_checks):
            ticket_error_rate += a_field
        ticket_checks.append(any(field_checks))
    if all(ticket_checks):
        valid_tickets.append(a_ticket)
#print(ticket_error_rate)        
possible_field_solutions = {}

for a_rule in rules:
    possibe_this_rule_solutions = []
    for column in range(0,20):
        checks = []
        for a_ticket in valid_tickets:
                this_check = ((a_ticket[column] >= rules[a_rule][0]) and (a_ticket[column] <= rules[a_rule][1])) or ((a_ticket[column] >= rules[a_rule][2]) and (a_ticket[column] <= rules[a_rule][3]))
                checks.append(this_check)
        if all(checks):
                possibe_this_rule_solutions.append(column)
                #break
    possible_field_solutions[a_rule] = possibe_this_rule_solutions

#print(possible_field_solutions)
field_solutions = {}
while len(field_solutions) < len(possible_field_solutions):
    for a_rule in possible_field_solutions:
        #print(possible_field_solutions[a_rule])
        if len(possible_field_solutions[a_rule]) == 1:
            solution_for_a_rule = possible_field_solutions[a_rule][0]
            field_solutions[a_rule] = solution_for_a_rule
            for some_rule in possible_field_solutions:
                if solution_for_a_rule in possible_field_solutions[some_rule]:
                    possible_field_solutions[some_rule].remove(solution_for_a_rule)

#print(field_solutions)

d_multiplied = 1

for a_rule in rules:
    if a_rule in field_solutions.keys():
        if 'departure' in a_rule:
            d_multiplied *= my_ticket[field_solutions[a_rule]]

print(d_multiplied)