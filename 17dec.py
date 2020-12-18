import copy

#import numba

initial_state = [    
"#.#..#.#",
"#.......",
"####..#.",
".#.#.##.",
"..#..#..",
"###..##.",
".#..##.#",
".....#..",
]

"""initial_state = [
".#.",
"..#",
"###",
]"""

# turn that list into a dictionary

the_cube = {}

for y in range(0,len(initial_state)):
    for x in range(0,len(initial_state[0])):
        the_cube[(x,y,0,0)] = initial_state[y][x]

#print(the_cube)  

x_range = [0,len(initial_state[0])]
y_range = [0,len(initial_state)]
z_range = [0,1]
w_range = [0,1]
mod_range = [-1,0,1]

# part one
cycles = 6

for cycle in range(0,cycles):
    active_count = 0
    input_cube = copy.deepcopy(the_cube)

    # move ranges
    x_range[0] -= 1
    x_range[1] += 1
    y_range[0] -= 1
    y_range[1] += 1
    z_range[0] -= 1
    z_range[1] += 1
    w_range[0] -= 1
    w_range[1] += 1
    #print(x_range)

    for x in range(x_range[0], x_range[1]):
        for y in range(y_range[0], y_range[1]):
            for z in range(z_range[0], z_range[1]):
                for w in range(w_range[0], w_range[1]):
                    # calculate surrounding active cubes
                    surrounding_active = 0
                    for x_mod in mod_range:
                        for y_mod in mod_range:
                            for z_mod in mod_range:
                                for w_mod in mod_range:
                                    if ((x+x_mod,y+y_mod,z+z_mod,w+w_mod) in input_cube) and ((x+x_mod,y+y_mod,z+z_mod,w+w_mod) != (x,y,z,w)):
                                        if input_cube[(x+x_mod,y+y_mod,z+z_mod,w+w_mod)] == "#":
                                            surrounding_active += 1
                    
                    if (x,y,z,w) in input_cube: # in cube prior to expansion, can be active
                        if (input_cube[(x,y,z,w)] == "#") and ((surrounding_active == 2) or (surrounding_active == 3)):
                            the_cube[(x,y,z,w)] = "#"
                            active_count += 1
                        elif (input_cube[(x,y,z,w)] == ".") and ((surrounding_active == 3)):
                            the_cube[(x,y,z,w)] = "#"
                            active_count += 1
                        else:
                            the_cube[(x,y,z,w)] = "."
                    else: # not in cube, in active
                        if ((surrounding_active == 3)):
                            the_cube[(x,y,z,w)] = "#"
                            active_count += 1
                        else:
                            the_cube[(x,y,z,w)] = "."
    #print(the_cube)
print(active_count)