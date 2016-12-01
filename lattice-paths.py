# Lattice paths
# Problem 15
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


# How many such routes are there through a 20x20 grid?


#solution using dynamic programing.
def lattice_paths(gs = 2):
    gs = 20
    grid = [[0 for x in range(gs+1)] for y in range(gs+1)]

    for k in range(len(grid)):
        grid[gs][k] = 1
        grid[k][gs] = 1


    for i in xrange(gs-1,-1,-1):  
        for j in xrange(gs-1,-1,-1):
            grid[i][j] = grid[i][j+1] + grid[i+1][j]

    return grid[0][0]


print lattice_paths(20)