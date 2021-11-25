from sudoku_grid import SudokuGrid

if __name__ == "__main__":
    solution = SudokuGrid(
        [
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9]
        ], 3
    )
    print(solution.get_block(2,3))
