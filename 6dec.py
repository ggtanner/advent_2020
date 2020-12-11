answers_text_raw = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\6dec_input.txt","r")

answers_data_text = []
this_group = []

for row in answers_text_raw:
    
    if row != "\n": #row has text
        this_group.append(row.replace("\n",""))
    else: #empty row
        #this_line_text = this_line_text.replace("\n", "")
        answers_data_text.append(this_group)
        this_group = []
# handle last line
if this_group != []:
    answers_data_text.append(this_group)

#print(answers_data_text)

alphabet = [
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
]

yes_count = 0

for a_group in answers_data_text:
    for letter in alphabet:
        this_letter_in_all = True
        for person in a_group:
            this_letter_in_all = this_letter_in_all and (letter in person)
        if this_letter_in_all:
            yes_count += 1

print(yes_count)