def execute_instructions(an_instructions_list):
    accumulator = 0
    instruction_to_execute = 0
    exucuted_instructions = []

    while (instruction_to_execute not in exucuted_instructions) and (instruction_to_execute < len(an_instructions_list)):
        this_instruction = instruction_to_execute
        
        if an_instructions_list[instruction_to_execute][0] == 'acc':
            accumulator += an_instructions_list[instruction_to_execute][1]
            instruction_to_execute += 1
        elif an_instructions_list[instruction_to_execute][0] == 'jmp':
            instruction_to_execute += an_instructions_list[instruction_to_execute][1]
        elif an_instructions_list[instruction_to_execute][0] == 'nop':
            instruction_to_execute += 1
        exucuted_instructions.append(this_instruction)
        
    reached_end_of_program = (instruction_to_execute == len(an_instructions_list))
    return [accumulator, reached_end_of_program]