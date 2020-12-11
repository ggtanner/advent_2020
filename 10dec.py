
from collections import defaultdict

input_file = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\10dec_input.txt","r")

adapters = input_file.readlines()

for adapter_index in range(0,len(adapters)):
    adapters[adapter_index] = int(adapters[adapter_index])
    
first_joltage = 0

max_joltage = max(adapters)

adapter_chain = [first_joltage]

diff_of_one  = 0
diff_of_three = 0

# part one 
while (len(adapter_chain) <= len(adapters)) and (max(adapter_chain) != max(adapters)):
    max_adapter = max(adapter_chain)
    if max_adapter + 1 in adapters:
        adapter_chain.append(max_adapter + 1)
        diff_of_one += 1
    elif max_adapter + 2 in adapters:
        adapter_chain.append(max_adapter + 2)
    elif max_adapter + 3 in adapters:
        adapter_chain.append(max_adapter + 3)
        diff_of_three += 1


print(diff_of_one * (diff_of_three + 1)) # +1 diff of 3 for the device internal converter

# part 2
adapters.append(0) # add outlet
adapters.append(max(adapters)+3) # add device internal adapter
adapters.sort() # sort highest to lowest

ways = defaultdict(lambda:0)
ways[0] = 1


for i in range(1, len(adapters)):
    ways[adapters[i]] = ways[adapters[i]-1] + ways[adapters[i]-2] + ways[adapters[i]-3]
    print(ways)
print(ways[adapters[-1]])


