

def trees_entountered(right_traverse,down_traverse):
    slope = [
    ".##.#.........#.....#....#...#.",
    ".#.#.#...#.......#.............",
    "......#..#....#.#...###.......#",
    ".......###......#.....#..##..#.",
    "..#...##.......#.......###.....",
    "....###.#....###......#....#..#",
    "......#..#....#...##...........",
    "..#..#....#...#.....####.......",
    "...#........#.#.......#..#...#.",
    "......#...#........#...#..##...",
    "#..#........#............#...##",
    "..#..#.#....#...........#...###",
    "#.#..#...........#.##.#.#....#.",
    ".#.#....#...##.....#...........",
    ".....##....#...#..............#",
    "...#....#...#.#.#.#...#........",
    "#....#....#.#.#..#....#..#..#..",
    ".................#..#.....#....",
    "#..###...#.#..#.#......#.......",
    "...#..........#......#....#....",
    ".#.#.........##..#.......#...#.",
    ".#..........#...#..#...........",
    "....##.#.......................",
    ".......#...........#...#.......",
    "...#...#..##...#....###..#....#",
    "....#.#.....##...##.#.#........",
    "...........#.#..#.#......#..#..",
    ".....#.....#....#...#........#.",
    "..#......#..#.........#.....#..",
    ".........................#...#.",
    "#...#...#....#........##....#..",
    "#..#.#.............#..........#",
    ".#.........#.....#..#.#.#..#.#.",
    "#...#..#.......####.#....##....",
    "##...##..#.#.#...#.#.....#..#.#",
    ".#..#....#.##........#...#....#",
    "#...#..##.#....##..#..#.#......",
    ".#........#.....#.#....##.##.#.",
    "...#...#........#..#.##.##.....",
    "....................#.#.#.#...#",
    "..####.#..##...#....#.....##...",
    "#......#.....#.#......#.#..#.##",
    "..#.....#..#...........##.#....",
    "#....#........#............#...",
    "..##....#..............#......#",
    "..#......#.#.......####......#.",
    "..............##....#....##.#..",
    ".#...............#....#....#.#.",
    "..#.#.#..#.......##.#..........",
    ".#...#.......#.#....#.##.......",
    ".....#.##...#...........#.#....",
    "..#.#..#...#..##...#.#.......##",
    ".#.....#....#.#......#.#.......",
    "....##.........#.#.............",
    ".......##.......#..............",
    "..........#......#......#....##",
    "..##.....#..#.#..........#.....",
    "...#....#.......#....##........",
    ".......#...........#...........",
    "...#.#......#.#........#....#..",
    ".....#...........#.#.#...#.#..#",
    ".#.#...#.#.#..........#.....###",
    "#........#...#.................",
    "...##.....#.....#..#..#.......#",
    "......##...........#..#....##..",
    ".........#............##...#...",
    ".....#.....##...##.............",
    ".#....#..#.#.#.#...#..#..#.....",
    ".....#..#.#..#....#..#.........",
    "....#.....#......#...#.........",
    "#..#..#.................#......",
    ".###.....#...#.#........##.#...",
    "..#...#....#.##..#.....#.#....#",
    "..#...##.................#.#...",
    "....##..........#..#..#..#....#",
    "....#..##....##.....#.#....#...",
    ".#.#.#.....##........#.##..##.#",
    "....#..#......#..#........#....",
    ".......#.....###.#....#.......#",
    "#....#.......#......##.#.......",
    ".##.#.........#.#..##..#....##.",
    "......#........#.#....#...#....",
    ".####.....#.........#.#......##",
    "##....#......#....#..#.#....##.",
    "...........###.#.....#..#......",
    ".......#...........#...........",
    "........###....#..#.#..........",
    "....#........#......#..........",
    ".........#......#..............",
    "...#...............#......#...#",
    "....#..##...#.........#...#....",
    "##........#.#....#......###....",
    "....#.......................#..",
    "#................#.#..#......##",
    "...#.#.....#...#...........#.##",
    ".#....#.##......#...##.#....#..",
    "#...#....#..............#..#..#",
    ".......#....#.##............#.#",
    ".....#.#.......#.#...#.........",
    "...#.....#..##...##...#........",
    "..#.......#..####..#..#...#....",
    "#.#................##...##.#..#",
    ".....#.....##.#.....#......#..#",
    "....#.#...#.........#.........#",
    "..#......#............#.....#..",
    ".....#..........#.#..#..##...##",
    "........#................#.#...",
    "#...#.#....##...###...#.#......",
    ".............##.#..##..........",
    "#..#......#...........#......#.",
    "#.#....#..........#.##....###..",
    ".............#.........#....#..",
    "#........#..#.#..#...#....#....",
    "..............#..............##",
    ".....#...#..............#.##...",
    "#...##..#...........#..........",
    "..#....#...#.#........#..#.#..#",
    "..##......#...............#....",
    "....#...#..###..#......###.#...",
    ".......##..#.#........#....#...",
    "..##...#.......#...#...........",
    ".#.......#.....#.#...##..#....#",
    ".............#.......#.#.#....#",
    "#.......#..#..#...#.#......##..",
    "#.##..#..#..#....##.#...###.#.#",
    "...##...#..#..#........#.#..#..",
    "#....##........................",
    "##...#...#......#.#.....#..#...",
    "......#............#....#......",
    "#......#.......#.......##.#....",
    "..................#..#..#.#....",
    "..#..................##.#......",
    "..##........#.#.....##..#..#.#.",
    "#....#..............#....####..",
    "#..#..........................#",
    "..#.#.#.#....#.......#....#.#..",
    ".....#.#........#..........#.#.",
    "........#.....#.......#........",
    "#.....#....#.###.....#.......#.",
    ".....##.#...#.#..#...#.#.#.....",
    "......##...#.#...##..........#.",
    ".#............#.....#..#....#..",
    ".#................#.#..#.......",
    "....................##...##....",
    "#.......##...#.....#..#........",
    ".##....#.#.#.#...........#...#.",
    "..#.#..#.#.........#...........",
    "...#......#.....#...##.........",
    "..........#.#.....###.#........",
    ".............#.....##..........",
    ".........#...####........#.####",
    "...................#....#......",
    ".....#.........#.#....#..#...#.",
    ".##...#.......##.#...#.#.#..#..",
    ".....##........#....#...#.##.#.",
    "#...#...#.#....#..............#",
    "#..#.##.............#..........",
    "..#...#..#.#.##..............##",
    "#......#.#...##..........#.##..",
    ".##.#...#...#.........#.#......",
    "......#........##.#..#.........",
    "#..#.......#......#.#..#.#.....",
    ".#..#...........#.#.##.....#...",
    ".....................#..#.#....",
    "........#...##......#.....##...",
    "#.............#...##....##....#",
    "#.#...........#....##.#......##",
    ".....#.....#.#..........###..#.",
    "....#...#....##....#..##.......",
    ".#....#....#.......#.#.....#...",
    ".#...#.......##...##........#..",
    "......##.......#.##.#.###......",
    "....##.......#......#..........",
    "...................#..##.......",
    "......................#...##...",
    "...##....#.#..#..#.............",
    ".#......##..........#...#......",
    "....##..#....#..#...#...####.#.",
    "...#.......#.......#........#.#",
    "#.........#..#...#...##...#.#.#",
    "....#...#.......#...#....#.....",
    "...#.....#.##..##.#.......##.##",
    ".......#....#........#.........",
    ".....#...#....#..#....#....#...",
    ".##....#...#........#...#.#...#",
    ".......##............#..#...#..",
    "#.#...#....#......#.#..........",
    ".#.##...........#........#.....",
    ".#....#.............#.#.##.....",
    "#.......###..#...###.........#.",
    "#..#.#.......#.........#...#..#",
    "..........#......#........#...#",
    ".#.#...#.##.......##...........",
    ".....#.........#.....#.........",
    ".........#.........#....##.#..#",
    ".#.......##..##..#.....#...#...",
    ".#.....##...#..#..............#",
    "..##...#..#..#.#...#..........#",
    ".#.......####......#......####.",
    "##..##........#.....#........#.",
    "..##.#..#.#....................",
    "...........#..#...##....##.....",
    "..#.#........#.........#....##.",
    "..#...#..##..###.#..###........",
    "......#..#.............#..##...",
    ".##.........#.#..#...#.##.###..",
    ".#...............#...........#.",
    ".#....#........#....#........##",
    "..#####.#.#..#.#........##...#.",
    "###....#....#...#..............",
    ".....#...##............#...#...",
    "##...........##.#.##.....#.....",
    "..............#..#.....#...#...",
    "...................#...........",
    "#..........##.........#........",
    "...#.........#..#.....#..#..#..",
    "....###.#......#......##....#..",
    "#......#..........#...#........",
    "...#.#...#..#..........##......",
    ".....##.....#.#............##..",
    "..#..#.###....#.#.#...##....#..",
    "...#........#....##.......#....",
    ".#.............#..##.......#...",
    "..#.#..###..#.....#...##.......",
    ".........#......##...#.#..#....",
    ".............#....##....#.#....",
    "#..#...#....#.#...#......##....",
    ".............#.#......#.....###",
    "#.##....#........#.............",
    ".....#...#.####...#.....#......",
    "....#....###....##.......#.....",
    "..#....##..#....#.#.......#....",
    "...#.....#....#.........#......",
    ".#......#.#....#.#........#....",
    ".......#......#.....#.#..#.....",
    "#......#.........##.##.#...#...",
    "..#.###...................#....",
    "....#..#....##.#........#....#.",
    "...........#..........#......#.",
    ".#..#.#...###..........#..#...#",
    "...#...##..#....#...#..........",
    ".#........#.................##.",
    "....#.......##....#...#........",
    "#.#...##.##...#.#.......#...#..",
    ".....#.#.##.#......#..#..##....",
    ".....##...#.#.....#...#........",
    "#.#.......#..#..........##.....",
    "................#......#..#.#.#",
    "#......#...#...................",
    "...#.....##.#.........#.#..#..#",
    "...#..##..##.......#....#......",
    "....##...#....#..#...........#.",
    "..#..#......#...#..#...........",
    "...#.##....#...##.......#......",
    ".......#....#..#..##..#..#....#",
    ".#.................#.#...#.##..",
    ".....#..................#..#.#.",
    "...#......##...#...........#...",
    "..#.........#....#..#...#.....#",
    "..#...#.....#.........##.#.....",
    ".....#.#....##...............#.",
    "....#...#............#.........",
    ".....#.....###............#....",
    "..#.#.#.......#....#...........",
    "...........##...##...#.......#.",
    ".........###.#......#..........",
    ".#.......#....#.....#.##..#...#",
    "..#..................#..###....",
    "..#....#...#......##.........#.",
    "........#..#........#.........#",
    ".#..#......#.........#.........",
    "...#..##.....#....#....#.....#.",
    "......#.#............###.....##",
    ".......#........#.......#.#....",
    "..#.............#..............",
    ".............##..#.#.#....#....",
    ".................#....#.#......",
    "##..#.#.......#....#.....#.....",
    ".##............##.#.......#.#..",
    "#..#...........##......#.......",
    ".##......#####..##.#....#.#....",
    ".......##.....#...#........#...",
    ".#.#.....##....#..#....#..#...#",
    "............##.#.....##.#......",
    "........##...###.#......#......",
    "......#..#.#...#..#............",
    ".........#...........#......#..",
    ".#.........#............##.....",
    ".#..#..#...#.#.............#...",
    "......#.#..##...#.#...........#",
    "#.##.......#...#.........#.....",
    ".....#..#............#....##...",
    ".#......#........#.............",
    "..#...#....#..#.......###......",
    "....#.......###.#.#...........#",
    ".............#...##............",
    ".##.#.#.#...........#...#....#.",
    "............##.........#......#",
    "...............#......#...#....",
    "...#.....#..###..#...........#.",
    ".#........#.....##........#.#..",
    "....#.#.......#..#..#...##.#.#.",
    ".......##...........#...#......",
    "....#.#..##......#.......#.....",
    "..#........#.#......#.#........",
    "........#....#..#....#..##.....",
    ".#.........##..........#.#.....",
    "..##...##.....##......##..#....",
    ".###.....##...........##.#...##",
    "...#................#.......#..",
    "#.......#.#.#..#.#.##..#...#...",
    ".#.#.......#..#................",
    "..#.#.#......#............#....",
    "#.....#.###..#.#...#...........",
    "#...........#..........#.#.#.##",
    "..#.#...#......##.....#........",
    "........#.......#.#...#...#....",
    "..#..........#......###......#.",
    "..........##.#....#.....#.##...",
    "..#.....#......#.........#..##.",
    ".#...#........#..#.#..#...##..#",
    "..###........#......#.#........",
    "..#.##.#....#.#....#.#...#.....",
    ]
    
    # expand slope until its big enough
    line = 0
    while line < len(slope):
        line_pattern = slope[line]
        while len(slope[line]) < ((right_traverse/down_traverse) * len(slope)):
            slope[line] = slope[line] + line_pattern 
        line += 1


    start_pos = [0,0]
    current_pos = start_pos
    end_pos = [len(slope[0]),len(slope)]
    print(end_pos)
    trees = 0

    while (current_pos[1] < end_pos[1]):
        if slope[current_pos[1]][current_pos[0]] == "#":
            trees += 1
        current_pos[0] += right_traverse
        current_pos[1] += down_traverse

    return(trees)

print(trees_entountered(1,1)*trees_entountered(3,1)*trees_entountered(5,1)*trees_entountered(7,1)*trees_entountered(1,2))