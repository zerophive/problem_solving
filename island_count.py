#!/usr/bin/env python3

# I saw this question in this video
# https://www.youtube.com/watch?v=cdCeU8DJvPM&feature=youtu.be
# 
# This got me curious to see how I would solve this. I guess you could call this a 
# kind of DFS solution, maybe, sort of. I have tested a couple of different matrices
# but really there are flaws and inefficienceies in this. O(n) is probably n^2 and
# and size complexity, yuk!

# 20200828 - I finally came across this on leetcode and wow, my previous solution
# was awful, it really only worked for the narrow examples I tried. It fails completely
# when other grids are used. It attempted to use too much, had way too much code
# and did not work, I read a few solutions and scratched my head and finally I figured
# it out. First I am an idiot, second, less is more, just need to think before I write
# I deleted 67 lines are garbage, the correct solution is 39 line, FML

sea = [
    [0,0,0,0,0],
    [1,1,0,0,0],
    [1,1,0,1,1],
    [0,0,0,1,0]
]

def num_of_island(grid):
    def search(row,col):
        if row < 0 or row >= len(grid): return
        if col < 0 or col >= len(grid[0]): return

        if grid[row][col] == 0: return

        island.append((row, col))
        grid[row][col] = 0

        search(row + 1, col)
        search(row, col + 1)
        search(row - 1, col)
        search(row, col - 1)


    islands = 0
    theIslands = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            island = []
            if grid[row][col] == 1:
                islands += 1
                search(row, col)

            if island: theIslands.append(island)

    return (islands, theIslands)

num_of_islands, islands = num_of_island(sea)
print("Number of islands: " + str(num_of_islands))
print("Islands: " + str(islands))
