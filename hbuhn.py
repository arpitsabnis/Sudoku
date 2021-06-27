import random
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def Solve_Sudoku(grid):

    count = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                count += 1

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                continue
            if count == 0:
                break
            k=1;
            bool = True;
            while(bool):
                if isSafe(grid,i,j,k):
                    bool=False
                    count=count-1
                    grid[i][j] = k
                k = k + 1;
                if k == 10:
                    bool = False
                # n= count-1
                # while count != n:
                #     value = random.randint(1,9)
                #     print(value)
                #     bool= isSafe(grid,i,j,value)
                #     print(bool)
                #     if isSafe(grid,i,j,value):
                #         count = count - 1
                #         grid[i][j] = value


def isSafe(grid, row, col, num):

    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True



Solve_Sudoku(grid)
for row in grid:
    for val in row:
        print '{:4}'.format(val),
    print
