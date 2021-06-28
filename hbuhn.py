import random
import numpy as np

def form_grid():
    """
    Prepares a SUDOKU
    """
    sudoku = []
    for i in range(9):
        arr = []
        for j in range(9):
            arr.append(0)
        sudoku.append(arr)
        
        ### Takes random 60 values and keeps other as zero ###

    for i in range(60): 
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        if i == 20 or i == 27:
            print(np.matrix(sudoku))
            print('row', row, 'col', col)
            num = input("Enter the number: ")
            valid = if_is_valid(sudoku, row, col, num)
            print(valid)
            if valid:
                sudoku[row][col] = num
            else:
                print('Number entered is not following sudoku rules')
            print(np.matrix(sudoku))
        while (not if_is_valid(sudoku, row, col, num) or sudoku[row][col] != 0):  # if taken or not valid reroll
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        sudoku[row][col] = num
    print("Sol: Final Matrix")
    print(np.matrix(sudoku))

def if_is_valid(sudoku, row, col, num):
    valid = True
    for x in range(9):
        if (sudoku[x][col] == num):
            valid = False

    for y in range(9):
        if (sudoku[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # check if section is validCheckValid
            if (int(sudoku[rowsection * 3 + x][colsection * 3 + y]) == int(num)):
                valid = False
                return valid
    return valid

form_grid()
