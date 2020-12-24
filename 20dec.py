input_file = open("C:\\Users\\Geoff\\Documents\\advent_of_code_2020\\20dec_input.txt","r")

input_lines = input_file.readlines()

tiles = {}
tile_lines = []

for a_line in input_lines:
    if ":" in a_line: # its a title line
        tile_title = a_line.replace(":\n", "")
    elif a_line == "\n": # its a break
         tiles[tile_title] = tile_lines

         tile_lines = []
    else:
        tile_lines.append(a_line.replace("\n", ""))

tile_edges = {}

for a_tile in tiles:
    a_tile_edges = {}
    
    a_tile_edges["top_edge"] = tiles[a_tile][0]
    a_tile_edges["bottom_edge"] = tiles[a_tile][-1]
    
    left_edge = ""
    right_edge = ""
    
    for image_line in tiles[a_tile]:
        left_edge = left_edge +image_line[0]
        right_edge = right_edge + image_line[-1]
        
    a_tile_edges["left_edge"] = left_edge
    a_tile_edges["right_edge"] = right_edge

    tile_edges[a_tile] = a_tile_edges

#print(tile_edges)

def check_match(tile_0,tile_1):
    matched_edges = [None, None, None]
    for edge_0 in tile_edges[tile_0]:
        for edge_1 in tile_edges[tile_1]:
            if (tile_edges[tile_0][edge_0] == tile_edges[tile_1][edge_1]):
                matched_edges = [edge_0, edge_1, "normal"]
                break
            elif (tile_edges[tile_0][edge_0] == tile_edges[tile_1][edge_1][::-1]):
                matched_edges = [edge_0, edge_1, "reversed"]
                break
    return matched_edges

matches = {}

for tile_0 in tiles:
    for tile_1 in tiles:
        if (tile_0 != tile_1) and (( (tile_0, tile_1) not in matches) and ( (tile_1, tile_0) not in matches) ):
            possible_match = check_match(tile_0,tile_1) 
            if possible_match != [None, None, None]:
                matches[(tile_0,tile_1)] = possible_match   

print(matches)
# find corners
"""corners = []
for tile in  tiles: 
    match_count = 0
    for match in matches:
        if tile in match:
            match_count += 1
    if match_count == 2:
        corners.append(tile)

print(corners)"""

#['Tile 2833', 'Tile 2557', 'Tile 3359', 'Tile 1367', ] -> No (too high)
#['Tile 2833', 'Tile 2557', 'Tile 1367', 'Tile 2239'] -> No (too low)
#[ 'Tile 2557', 'Tile 3359', 'Tile 1367', 'Tile 2239'] -> No (too low)
corners = ['Tile 2833', 'Tile 3359', 'Tile 1367', 'Tile 2239'] # -> correct!

# look at corners... bottom left should have a top and right match, etc
for corner in corners:
    for match in matches:
        if corner in match:
            print(match)
            print(matches[match])

