import copy 

lobby_map = [
"LLLLLLLLL.L.LLL.L.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LLL.LLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"L..LL.L.L....L..L.L....L.....L.L.L......L..L..L....L.LL.......L.....L....L..L................L....",
"LLLLLLLLLLLLLLL.LLL.LLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL..LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLLLLLL.LLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLL.LLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
"LL.LLLLLLLLLLLL.LLL.LLL.LLLLLLLL.LLLLLLLL.LLLLLLL..LLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLL.LL.LLLLLLLL",
"LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLL.L.LLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLLLL",
".LLLL..L.L..L....L.LLL...LLL..L.L....L.L.L...L.....L...L.....L...L..L...LL...L..LLL..L...L....L..L",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL",
"LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLL..LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL..LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
".....LL...LL..L...L..L..LL.L..LLL...L..L.LLL...LLL..L.....L...L.....L........LLLL..LLL.....L....L.",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LL",
"LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLL.L",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLL.LLLLLLLLL.LLLLLLL.LLLL.LLL.LL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLL.LLLLLLLL",
"....L..LL.L.L......L..LL.......LL......L..L...L..L.........LL....LL.LLL..LLLL..L..L.......L....L..",
"LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLL.LLL.L.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLL.LLLLLLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
".LL..LLLLL.LL.L...L...L...L....LLLL...LLLL.LL...LL...L.LL...LL..LL.L..L......L....L.L.L.L...LL...L",
"LLLLLLLLL.LLLLLLLLLLLLL..LLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLLLL",
"LLLLLLLLL.LLLLL.L.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLL..LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LL.LL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLL.LLLLL.L.LLLLLLLL",
"....L.........LL...L.L..LL.L.L..L......L.L.L...L....L.......LL.LL....L.L...L....L...L....L...L....",
"L.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LL..LLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLL..LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.L.LLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLL.LL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"LLL..L.L........L...L..L.LLLLLLL..LLLL..L...L..L.L..LLL....L..L.LLL..L...L..L.......L.LLLLLL.LL.L.",
"LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LL.LLLL.LLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LL.LL.LLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
"L...L.....LL....L.L.LLLLL.....L....LL..L.....L...L.L.LL.......LL...LL............L.L..L..LLL..LL..",
"LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LL",
"LL.LLLLLLLLLLLL.L.LLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLL.LLLLLL.LLLLL.LLLLLLL.L.LLLLLL",
"LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLL.LLLL",
"LLLLLLLLL.LLLLL.L.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLL",
"LLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLL..LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LL...L.........L..LLL........L.L..L....L.L.L....LLLL.LL.L....LL....L.LL.LLL..L..L....LL.L......LLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLL.L.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
"...L........L....L.L.LL.LL.L.L.....L.L..L.....LL....L..L.L.L..L..L.L...L.........L.LL.LLLLL..L....",
"LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL..LLLL.LLLLLLL.LLLLLLLLLLL.LLL.L.LLLLLLLLLLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.L.LLLLLLLL",
"LLLLLLLLL.LLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL..LLLLLLL",
"LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"..LLLL.L..LL.L......LL.L...L.L..L....LLL.........L....L.......LL.LLL.L.L.....LL.L...L.LLL....L....",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.L.LLL.LLLLLLL.LLLL.LLLLLL.LLLL..LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLLL.L.LLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLLLLLLL.LL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"LL...LLLLL.....LL..L.....L....L......L.L........LL......LL.LL..L..LLL.L...L..L..L.L.....LLLL...LLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLL.LLLLL.LLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
".LL..L.....LLLL.LL..L.LL....L.LL...L..LL......L..LL...LL..L.L.LLLL...LL.L..L..LLL.L.L.....L.LL.LL.",
"LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLL.LLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLL.LL",
"LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL",
"LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
"LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLL.L.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL",
]

output_room = []
for line in lobby_map:
    output_room.append(list(line))

#print(lobby_map)

input_room = [] # to make not equal to start
#output_room = copy.deepcopy(lobby_map) 

"""#part i
while input_room != output_room:
    input_room = copy.deepcopy(output_room)
    for row in range(0,len(output_room)):
        for column in range(0,len(output_room[row])):
            # check loss
            los_count = 0
            if column > 0:
                if input_room[row][column -1] == "#":
                    los_count += 1
            if column < (len(output_room[row]) -1):
                if input_room[row][column +1] == "#":
                    los_count += 1
            if (column > 0) and (row > 0):
                if input_room[row -1][column -1] == "#":
                    los_count += 1
            if (column < (len(output_room[row])-1)) and (row > 0):
                if input_room[row -1][column +1] == "#":
                    los_count += 1
            if (column > 0) and (row < (len(input_room) -1 )):
                if input_room[row +1][column -1] == "#":
                    los_count += 1
            if (column < (len(output_room[row])-1)) and (row < (len(input_room) -1 )):
                if input_room[row +1][column +1] == "#":
                    los_count += 1
            if (row > 0):
                if input_room[row -1][column] == "#":
                    los_count += 1
            if (row < (len(input_room) -1 )):
                if input_room[row +1][column] == "#":
                    los_count += 1
    
            if (input_room[row][column] == "L") and los_count == 0: # if seat is empty and no los seats
                #print(output_room[row][column])
                output_room[row][column] = '#'
                #print(print(output_room[row][column]))
            elif (input_room[row][column] == '#') and los_count >= 4: # If a seat is occupied (#) and four or more seats los to it are also occupied, the seat becomes empty
                output_room[row][column] = 'L'
            else:
                #output_room[row][column] = input_room[row][column]
                pass"""

# part ii
iteration = 0
while input_room != output_room:
    input_room = copy.deepcopy(output_room)
    for row in range(0,len(output_room)):
        for column in range(0,len(output_room[row])):
            # check line of site
            los_count = 0
            # left
            found_los = False
            rel_x = 0 
            rel_y = 0 
            while (not found_los) and ((column + rel_x) >= 0):
                found_los = (input_room[row][column + rel_x] == "#")
                if found_los:
                    los_count += 1
                else:
                    rel_x -= 1 
            # right
            found_los = False
            rel_x = 0 
            rel_y = 0 
            while (not found_los) and ((column + rel_x) < len(output_room[row])):
                found_los = (input_room[row][column + rel_x] == "#")
                if found_los:
                    los_count += 1 
                else:
                    rel_x += 1 
            # up
            found_los = False
            rel_x = 0 
            rel_y = 0 
            while (not found_los) and ((row + rel_y) >= 0):
                found_los = (input_room[row + rel_y][column] == "#")
                if found_los:
                    los_count += 1 
                else:
                    rel_y -= 1 
            # down
            found_los = False
            rel_x = 0 
            rel_y = 0 
            while (not found_los) and ((row + rel_y) < len(output_room)):
                found_los = (input_room[row + rel_y][column] == "#")
                if found_los:
                    los_count += 1 
                else:
                    rel_y += 1 

            # up left
            found_los = False
            rel_x = 0 
            rel_y = 0 
            while (not found_los) and ((row + rel_y) >= 0) and ((column + rel_x) >= 0):
                found_los = (input_room[row + rel_y][column + rel_x] == "#")
                if found_los:
                    los_count += 1 
                else:
                    rel_y -= 1 
                    rel_x -= 1
            # up right
            found_los = False
            rel_x = 0 
            rel_y = 0 
            while (not found_los) and ((row + rel_y) >= 0) and ((column + rel_x) < len(output_room[row])):
                found_los = (input_room[row + rel_y][column + rel_x] == "#")
                if found_los:
                    los_count += 1 
                else:
                    rel_y -= 1 
                    rel_x += 1
            # down left
            found_los = False
            rel_x = 0 
            rel_y = 0
            while (not found_los) and ((row + rel_y) < len(output_room)) and ((column + rel_x) >= 0):
                found_los = (input_room[row + rel_y][column + rel_x] == "#")
                if found_los:
                    los_count += 1 
                else:
                    rel_y += 1 
                    rel_x -= 1
            # down right
            found_los = False
            rel_x = 0 
            rel_y = 0
            while (not found_los) and ((row + rel_y) < len(output_room)) and ((column + rel_x) < len(output_room[row])):
                found_los = (input_room[row + rel_y][column + rel_x] == "#")
                if found_los:
                    los_count += 1 
                else:
                    rel_y += 1 
                    rel_x += 1 

    
            if (input_room[row][column] == "L") and los_count == 0: # if seat is empty and no los seats
                #print(output_room[row][column])
                output_room[row][column] = '#'
                #print(print(output_room[row][column]))
            elif (input_room[row][column] == '#') and los_count >= 5: # If a seat is occupied (#) and four or more seats los to it are also occupied, the seat becomes empty
                output_room[row][column] = 'L'
            else:
                #output_room[row][column] = input_room[row][column]
                pass
            #print("iterating row "+ str(row) + "/" + str(len(input_room)) +" ; column "+ str(column)+ "/" + str(len(input_room[row])))
    iteration += 1
    print("this is iteration # " + str(iteration))

occupied_count = 0
for row in output_room:
    for column in row:
        if column == "#":
            occupied_count += 1

print(occupied_count)




            
