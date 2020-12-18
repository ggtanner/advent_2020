import copy

input_file = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\14dec_input.txt","r")
program = input_file.readlines()

current_mask = ''
memory = {}


"""part 1
for line in program:
    #print(line)
    if 'mask' in line:
        mask_str = line.replace("mask = ", "")
        current_mask = mask_str
    if 'mem' in line:
        mem_str = line
        mem_str = mem_str.replace('mem[', '')
        mem_str = mem_str.replace(']', '')
        mem_str = mem_str.replace(' ', '')
        mem_array = mem_str.split('=')
        address = int(mem_array[0])
        value = mem_array[1]
        
        address_bin = bin(int(value))[2:]

        while (len(address_bin) < (len(current_mask) -1)):
            address_bin = '0' + address_bin
        
        print(address_bin)
        print(current_mask)
        address_bin = list(address_bin)
        for bit in range(0,len(address_bin)):
            if current_mask[bit] == 'X':
                pass
            elif current_mask[bit] == '1':
                address_bin[bit] = '1'
            elif current_mask[bit] == '0':
                address_bin[bit] = '0'

        value_out = ''
        value_out = value_out.join(address_bin)
        memory[address] = int(value_out, 2)
"""

# part ii
sum_in_memory = 0
for line in program:
    print(line)
    if 'mask' in line:
        mask_str = line.replace("mask = ", "")
        current_mask = mask_str
    if 'mem' in line:
        mem_str = line
        mem_str = mem_str.replace('mem[', '')
        mem_str = mem_str.replace(']', '')
        mem_str = mem_str.replace(' ', '')
        mem_array = mem_str.split('=')
        address_prog = int(mem_array[0])
        value = int(mem_array[1])
        
        address_bin = bin(int(address_prog))[2:]

        while (len(address_bin) < (len(current_mask) -1)):
            address_bin = '0' + address_bin
        
        #print(address_bin)
        #print(current_mask)
        address_bin = list(address_bin)
        x_count = 0
        for bit in range(0,len(address_bin)):
            if current_mask[bit] == 'X':
                address_bin[bit] = 'X'
                x_count += 1
            elif current_mask[bit] == '1':
                address_bin[bit] = '1'
            elif current_mask[bit] == '0':
                address_bin[bit] = '0'
        possible_addresses = [address_bin]
        x_check = False
        while not x_check:
            x_check_array = []
            for address in possible_addresses:
                if 'X' in address:
                    pass
                for bit in range(0,len(address)):
                    if address[bit] == 'X':
                        address_0 = copy.deepcopy(address)
                        address_1 = copy.deepcopy(address)
                          
                        address_0[bit] = '0'
                        address_1[bit] = '1'

                        possible_addresses.append(address_0)
                        possible_addresses.append(address_1)
                        #print(possible_addresses)
            for address in possible_addresses:
                x_check_array.append('X' in address)
            x_check = all(x_check_array)
            print(x_check)

        for address in possible_addresses:
            memory[address] = value 
        possible_addresses = []
sum_in_memory = 0        
for location in memory:
    sum_in_memory += memory[location]
print(sum_in_memory)

