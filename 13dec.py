from time import time

earliest_time = 1001798
x = None
buses = [19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,859,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37]

"""# part one
bus_catching_dict = {}

for bus in buses:
    if bus == None:
        pass #this bus is out of service
    else:
        next_time_for_bus = (int(earliest_time/bus) + 1) * bus  # next catchable bus is (1+ (earliest time / bus interval)) * bus interval
        bus_catching_dict[bus] = [next_time_for_bus - earliest_time]

print(bus_catching_dict)"""

# part two
t = 0
bus_ids = []
bus_offsets = []

for bus_index in range(0,len(buses)):
    if buses[bus_index] == None:
        pass
    else:
        bus_ids.append(buses[bus_index])
        bus_offsets.append(bus_index)

print (bus_ids)
print (bus_offsets)

condition_met = False

t_0 = time()

while not condition_met:
    checks = []
    for bus in range(0,len(bus_ids)):
        checks.append((t + bus_offsets[bus])%bus_ids[bus] == 0)
    
    condition_met = all(checks)
    if condition_met:
        print("time " + str(t) + " is earliest with specified order")
    else:
        loop_incrementor = 1
        for i in range(0, len(checks)):
            if checks[i] == True:
                loop_incrementor *= bus_ids[i]
        t += loop_incrementor 

t_1 = time()

print(str(t_1 - t_0))