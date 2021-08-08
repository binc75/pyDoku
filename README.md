## Sudoku solver
Using backtracking/recursion to solve sudoku puzzles.

### Backtrackin & Recursion
```python
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

            # backtracking: if not valid or if nothing gets returned true, then we need to backtrack and try a new number
            bo[row][col] = 0

    return False
```

### Output example
```
Sudoku 1
-------------------------------
|  0 0 7  |  0 4 0  |  0 0 0  |
|  0 0 0  |  0 0 8  |  0 0 6  |
|  0 4 1  |  0 0 0  |  9 0 0  |
-------------------------------
|  0 0 0  |  0 0 0  |  1 7 0  |
|  0 0 0  |  0 0 6  |  0 0 0  |
|  0 0 8  |  7 0 0  |  2 0 0  |
-------------------------------
|  3 0 0  |  0 0 0  |  0 0 0  |
|  0 0 0  |  1 2 0  |  0 0 0  |
|  8 6 0  |  0 7 0  |  0 0 5  |
-------------------------------
Solution Sudoku 1
-------------------------------
|  9 8 7  |  6 4 2  |  5 3 1  |
|  2 3 5  |  9 1 8  |  7 4 6  |
|  6 4 1  |  5 3 7  |  9 8 2  |
-------------------------------
|  5 2 6  |  3 8 4  |  1 7 9  |
|  1 7 3  |  2 9 6  |  8 5 4  |
|  4 9 8  |  7 5 1  |  2 6 3  |
-------------------------------
|  3 1 9  |  8 6 5  |  4 2 7  |
|  7 5 4  |  1 2 3  |  6 9 8  |
|  8 6 2  |  4 7 9  |  3 1 5  |
-------------------------------
```
