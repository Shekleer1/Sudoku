

sudoku = [[0,1,9,0,0,6,0,0,0],
          [2,0,8,3,1,0,5,0,6],
          [0,6,0,0,7,0,0,1,0],
          [9,3,5,6,0,1,7,2,4],
          [1,8,7,0,0,4,0,5,3],
          [0,2,4,8,0,0,0,0,9],
          [8,5,2,0,6,0,0,3,0],
          [0,0,0,1,0,0,2,0,8],
          [0,9,0,0,2,7,4,6,0]]


def possible(y, x, n):
    global sudoku
    for i in range(9):
        if sudoku[y][i] == n:
            return False
    for i in range(9):
        if sudoku[i][x] == n:
            return False
    x0 = (x // 3)*3
    y0 = (y // 3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[y0 + i][x0 + j] == n:
                return False
    else:
        return True

