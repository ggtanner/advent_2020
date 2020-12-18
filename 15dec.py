import copy
import numpy as np
from numba import jit
from time import time



starter_numbers = [2,1,10,11,0,6]
#starter_numbers = [0,3,6]



last_index_for_value = {}
all_numbers = {}
for an_index in range(0,len(starter_numbers)):
    all_numbers[an_index] = starter_numbers[an_index]
    last_index_for_value[starter_numbers[an_index]]  = an_index
last_turn = len(all_numbers)

time_0 = time()

jit(nopython=True)

while last_turn < 2020:
    
    last_number = all_numbers[last_turn - 1] # last number, including starter numbers
    
    if sum(x == last_number for x in all_numbers.values()) == 1:
        current_number = 0
        last_index_for_value[last_number] = last_turn
    else:   
        # need new way to search
        
        previous_turn_with_number = last_index_for_value[last_number] + 1
        current_number = last_turn - previous_turn_with_number

    all_numbers[last_turn] = current_number

    if last_number in last_index_for_value.keys():
        last_index_for_value[last_number] = last_turn -1
        #print(last_index_for_value)
        #print(all_numbers)
    last_turn = len(all_numbers)

#print(spoken_numbers)
time_1 = time()
print(all_numbers)
print( ((time_1 - time_0)/2020)*(30000000/60/60))

