#!/usr/bin/env python3

# I saw this question in this video
# https://www.youtube.com/watch?v=cdCeU8DJvPM&feature=youtu.be
# 
# This got me curious to see how I would solve this. I guess you could call this a 
# kind of DFS solution, maybe, sort of. I have tested a couple of different matrices
# but really there are flaws and inefficienceies in this. O(n) is probably n^2 and
# and size complexity, yuk!

sea = [
    [0,0,0,0,0],
    [1,1,0,0,0],
    [1,1,0,1,1],
    [0,0,0,1,0]
]

def num_of_island(grid):
    total_islands = 0
    islands = []

    col_len = len(grid)
    row_len = len(grid[0])
    


    def check_below(element, island):
        lower_neighbour = element[0] + 1
        if lower_neighbour > col_len - 1: return island
        if grid[lower_neighbour][element[1]] == 1:
            island = add_island((lower_neighbour, element[1]), island)
            island = check_left(island[-1], island)
            island = check_right(island[-1], island)
            return check_below(island[-1], island)
        else:
            return island

    def check_right(element, island):
        right_neighbour = element[1] + 1
        if right_neighbour > row_len - 1: return island
        if sea[element[0]][right_neighbour] == 1:
            island = add_island((element[0], right_neighbour), island)
            island =  check_below(island[-1], island)
            return check_right(island[-1], island)
        else:
            return island
            
    def check_left(element, island):
        left_neighbour = element[1] - 1
        if left_neighbour < 0: return island
        if sea[element[0]][left_neighbour] == 1:
            island = add_island((element[0], left_neighbour), island)
            island = check_below(island[-1], island)
            return check_left(island[-1], island)
        else:
            return island

    def add_island(element, island):
        if not element in island:
            island.append(element)
            sea[element[0]][element[1]] = 0
            #print(sea)
        
        return island

    row_count = 0
    for row in grid:
        island = []
        if row.count(1) == 0:
            row_count += 1
            continue
        for element in range(col_len):
            if grid[row_count][element] == 1:
               island = add_island((row_count,element), island)
               island = check_below((row_count,element), island)
               island = check_right((row_count,element), island)
        row_count += 1
        islands.append(island)
    
    return len(islands), islands

num_of_islands, islands = num_of_island(sea)
print("Number of islands: " + str(num_of_islands))
print("Islands: " + str(islands))
