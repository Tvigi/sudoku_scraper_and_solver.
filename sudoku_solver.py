from sudoku_scraper import scrape

def print_sudoku(sudoku_grid):
    for i in range(9):
        for j in range(9):
            print(str(sudoku_grid[i][j])+' ', end='')
        print()

#provjerava moze li se u redu sa indexom row i u koloni sa indexom col dodati broj num
def can_add(sudoku_grid, row, col, num):
    #prvo treba provjeriti da li se taj broj vec nalazi u tom redu
    for i in range(9):
        if sudoku_grid[row][i] == num:
            return False
    
    #treba provjeriti da li se vec nalazi u toj koloni
    for i in range(9):
        if sudoku_grid[i][col] == num:
            return False

    #treba naci odgovarajuci 3*3 kvadrat u kojem se nalazi
    #takodje treba provjeriti da li se tu nalazi
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if sudoku_grid[start_row+i][start_col+j] == num:
                return False

    return True

def solve_sudoku(sudoku_grid, row, col):
    if row == 8 and col == 9:
        return True
    
    if col == 9:
        row += 1
        col = 0

    if sudoku_grid[row][col] > 0:
        return solve_sudoku(sudoku_grid, row, col+1)

    for num in range(1, 10):

        if can_add(sudoku_grid, row, col, num):
            sudoku_grid[row][col] = num
            
            if solve_sudoku(sudoku_grid, row, col+1):
                return True

            sudoku_grid[row][col] = 0
    
    return False

sudoku_grid = scrape()
solve_sudoku(sudoku_grid, 0, 0)
print_sudoku(sudoku_grid)