from gameyoungling import *

instructions_raw = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\8dec_input.txt","r")

instructions_list = []

for instruction in instructions_raw:
    instruction = instruction.replace("\n", "")
    instruction = instruction.split(" ")
    instruction[1] = int(instruction[1])
    instructions_list.append(instruction)

#print(instructions_list)

#print(execute_instructions(instructions_list))

for instruction_index in range(0,len(instructions_list),1):
    instructions_raw = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\8dec_input.txt","r")

    instructions_list = []

    for instruction in instructions_raw:
        instruction = instruction.replace("\n", "")
        instruction = instruction.split(" ")
        instruction[1] = int(instruction[1])
        instructions_list.append(instruction)
    prospective_instructions = instructions_list    

    if prospective_instructions[instruction_index][0] == 'nop':
        prospective_instructions[instruction_index][0] = 'jmp'
        execution_results = execute_instructions(prospective_instructions)
        evauluate_results = True
    elif prospective_instructions[instruction_index][0] == 'jmp':
        prospective_instructions[instruction_index][0] = 'nop'
        execution_results = execute_instructions(prospective_instructions)
        evauluate_results = True
    else:
        evauluate_results = False

    if evauluate_results:
        if execution_results[1]:
            print(execution_results)    

