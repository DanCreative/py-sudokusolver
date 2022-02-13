from dataclasses import dataclass

class SudokuGridRowError(Exception):
    def __str__(self) -> str:
        return f"All Sudoku rows must be the same lenght."
class SudokuGridBlockError(Exception):
    def __str__(self) -> str:
        return f"All blocks must be the same size and complete"
class SudokuGridEmptyError(Exception):
    def __str__(self) -> str:
        return f"SudokuGrid can't be empty"  

class SudokuGrid():
    def __init__(self, rows: list[list]):
        self.side_lenght = len(rows)
        self.block_size = int(self.side_lenght ** (0.5))
        self.rows = rows
        self.history = []
        self.is_solvable = None
    def update_grid(self, x: int, y: int, new_val:int, old_val:int):
        if self.rows[x][y] > 0:
            self.history.append(SudokuGridChange(type=0,x=x,y=y,new_value=new_val, old_value=old_val))
        else:
            self.history.append(SudokuGridChange(type=1,x=x,y=y,new_value=new_val, old_value=old_val))
        self.rows[x][y] = new_val
    def solve(self):
        self.is_solvable = self.is_solved()
        if self.is_solvable:
            print(self)
        else:
            print("No solution found")
    def is_solved(self, p_row = 0, p_col = 0):
        #If reach end of the Sodoku grid, return True. Grid solved
        if (p_row == self.side_lenght - 1 and p_col == self.side_lenght):
            return True

        #If end of row has been reached, continue to next row
        if (p_col == self.side_lenght):
            p_row += 1
            p_col = 0
        
        #If number is not empty, continue to next number in row
        if self.rows[p_row][p_col] > 0:
            return self.is_solved(p_row, p_col + 1)

        #loop through numbers to insert in grid
        for num in range(1, self.side_lenght + 1):

            #If number is valid, insert into grid
            if self.is_valid(self.rows, p_row, p_col, num):
                self.update_grid(p_row, p_col, num, self.rows[p_row][p_col])

                #If number is valid, Go to the next column
                if self.is_solved(p_row, p_col + 1):
                    return True

            #Reset value back to 0 if not valid
            self.update_grid(p_row, p_col, 0, self.rows[p_row][p_col])
        return False     
    def is_valid(self, p_grid, p_row, p_col, p_num):
        is_valid = True
        col_start = p_col - p_col % self.block_size
        row_start = p_row - p_row % self.block_size

        for row_i, row in enumerate(p_grid):
            for col_i, col in enumerate(row): 
                if row_i == p_row and p_num == col:
                    is_valid = False

                if col_i == p_col and p_num == col:
                    is_valid = False

                if (col_start <= col_i < col_start + self.block_size) and (row_start <= row_i < row_start + self.block_size) and (p_num == col):
                    is_valid = False

        return is_valid 
    def __str__(self) -> str:
        out = ""
        for i, row in enumerate(self.rows):
            out+=" | ".join(map(str,row))+"\n"
            if ((i+1) % self.block_size == 0): 
                out += "---------------------------------\n"
                
        return out

@dataclass
class SudokuGridChange():
    type: int #type: 0-REVISION, 1-NEW
    x: int
    y: int
    new_value: int
    old_value: int