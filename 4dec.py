passport_text_raw = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\4dec_input.txt","r")

passport_data_text = []
this_line_text = ""

for row in passport_text_raw:
    
    if row != "\n": #row has text
        this_line_text = this_line_text + row + " "
    else: #empty row
        this_line_text = this_line_text.replace("\n", "")
        passport_data_text.append(this_line_text)
        this_line_text = ""
# handle last line
if this_line_text != "":
    passport_data_text.append(this_line_text)

#print(passport_data_text)

valid_passport_fields = [
    "byr", # (Birth Year)
    "iyr", # (Issue Year)
    "eyr", # (Expiration Year)
    "hgt", # (Height)
    "hcl", # (Hair Color)
    "ecl", # (Eye Color)
    "pid", # (Passport ID) 
    #"cid", # (Country ID) ignored per problem
]

valid_passport_count = 0

for a_passport_text in passport_data_text:
    
    valid_passport = None
    for a_field in valid_passport_fields:
        check_field = a_field + ":"
        if valid_passport == None: # first field to check
            valid_passport = (check_field in a_passport_text)
            
        else: # any other field
            valid_passport = (valid_passport and (check_field in a_passport_text))
    if valid_passport:
        """
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:

    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.

hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
        """
        fields = dict(item.split(':') for item in a_passport_text.split())
        byr_test = (1920 <= int(fields['byr']) <= 2002) and (len(fields['byr']) == 4)
        iyr_test = (2010 <= int(fields['iyr']) <= 2020) and (len(fields['iyr']) == 4)
        eyr_test = (2020 <= int(fields['eyr']) <= 2030) and (len(fields['eyr']) == 4)
        if 'in' in fields['hgt']:
            height_val = int(fields['hgt'][:-2])
            hgt_test = 59 <= height_val <= 76
        elif 'cm' in fields['hgt']:
            height_val = int(fields['hgt'][:-2])
            hgt_test = 150 <= height_val <= 193
        else:
            hgt_test = False
        if fields['hcl'][0] == "#" and (len(fields["hcl"][1:]) == 6):
            hcl_test = int(fields['hcl'][1:],16) > 0
        else:
            hcl_test = False 
        accepted_ecls = ["amb", "blu" ,"brn", "gry", "grn", "hzl", "oth"]
        ecl_test = (fields["ecl"] in accepted_ecls)
        
        if len(fields['pid']) == 9:
            pid_test = fields['pid'].isnumeric()
        else:
            pid_test = False
        if pid_test and ecl_test and hcl_test and hgt_test and eyr_test and iyr_test and byr_test:
            valid_passport_count += 1
        #print(fields)
print(valid_passport_count)    