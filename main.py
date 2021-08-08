#!/usr/bin/env python3

# Initial sudoku board (empty spaces)
board = [
    [0, 0, 7, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 6],
    [0, 4, 1, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 7, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 8, 7, 0, 0, 2, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0, 0],
    [8, 6, 0, 0, 7, 0, 0, 0, 5]
]

board2 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

hardest_sudoku = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]]


# Pretty print the sudoku board
def print_sudoku(bo):
    '''Print the board'''
    # for the number of lists in the board: 9 in this case
    for row in range(len(bo)):
        if row == 0:
            print('-' * 31)
        # for the number of elements of a list inside the board: 9 in this case
        for col in range(len(bo[0])):
            if col == 0:
                print("| ", end=' ')
            print(bo[row][col], end=' ')
            if col + 1 == 3 or col + 1 == 6 or col == 8:
                print(" | ", end=' ')
        if row + 1 == 3 or row + 1 == 6:
            print("\n" + "-" * 31, end=' ')
        print()
    print('-' * 31)


# Check if a guessed number is valid for the given position in the sudoku board
def check_valid_guess(bo, row, col, num):

    # check row
    if num in bo[row]:
        return False

    # check col
    current_col = []
    for x in range(len(bo)):
        current_col.append(bo[x][col])

    if num in current_col:
        return False

    # check box
    current_box = []
    start_row = row // 3  # floor division by 3 to get the current box row
    start_col = col // 3  # floor division by 3 to get the current box col

    # looping 3x3 from the beginning of the wanted box
    for x in range(3):
        for y in range(3):
            current_box.append(bo[x + start_row * 3][y + start_col * 3])

    if num in current_box:
        return False

    # if at this point nothing is False, return true
    return True


# Check next empty space in the sudoku board
def next_empty(bo):
    for x in range(len(bo)):
        for y in range(len(bo[0])):
            if bo[x][y] == 0:
                return (x, y)

    return None  # if no more spaces are empty


# Solver
def solve(bo):
    # check next empty space in the sudoku board
    next = next_empty(bo)
    # if next is populated, assing the tuple value to the 2 vars row, col
    if next:
        row, col = next
    else:
        return True

    # for empty slots try ...
    for i in range(1, 10):
        # if i is a valid guess assing to the board slot
        if check_valid_guess(bo, row, col, i):
            bo[row][col] = i

            # recursion: we recursively call our solver
            if solve(bo):
                return True

            # backtracking: if not valid or if nothing gets returned true, then
            # we need to backtrack and try a new number
            bo[row][col] = 0

    return False


# Solutions
print("Sudoku 1")
print_sudoku(board)
print("Solution Sudoku 1")
solve(board)
print_sudoku(board)

print("Sudoku 2")
print_sudoku(board2)
print("Solution Sudoku 2")
solve(board2)
print_sudoku(board2)

print("Sudoku 3")
print_sudoku(hardest_sudoku)
print("Solution Sudoku 3")
solve(hardest_sudoku)
print_sudoku(hardest_sudoku)
