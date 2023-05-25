import numpy as np


sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,0,0]]


def main(x, y, n):                             #
    global sudoku                              # Sudoku matrix is global, hasn't needed to be
    for i in range(9):                         # 9 is a value of raw's, and column's
        if sudoku[x][i] == n:                  # Using coordinate's to point a specific value is matrix
            return False                       #
    for i in range(9):                         # We should imagine whole structure as a 9 square's contains
        if sudoku[i][y] == n:                  # values which we get by ------------[0.0][0.1][0.2]
            return False                       # dividing eny pair of a coordinates [1.0][1.1][1.2]
    x0 = (x // 3)*3                            # by 3 'x = (x // 3) & y = (y // 3)' [2.0][2.1][2.2]
    y0 = (y // 3)*3                            # so that we specify square in which we should check
    for i in range(3):                         # values; In the next step we define starting point
        for j in range(3):                     # from which beginning to check every value in previously
            if sudoku[x0 + i][y0 + j] == n:    # detected square, doing it simply by multiply our x & y
                return False                   # values by 3 'x0 = (x // 3)*3 & y0 = (y // 3)*3'
    else:                                      # Checking by simple matching value's using our
        return True                            # new created coordinates


def solve():
    global sudoku
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                for n in range(1, 10):
                    if main(x, y, n):
                        sudoku[x][y] = n
                        solve()
                        sudoku[x][y] = 0
                return
    print(np.matrix(sudoku))
    input('More? ')

solve()
