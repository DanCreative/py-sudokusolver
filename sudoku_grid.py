class SudokuGridRowError(Exception):
    def __str__(self) -> str:
        return f"All rows must be the same lenght"

class SudokuGridBlockError(Exception):
    def __str__(self) -> str:
        return f"All blocks must be the same size and complete"

class SudokuGridXOutOfRange(Exception):
    def __str__(self) -> str:
        return f"X coordinate is out of range"

class SudokuGridYOutOfRange(Exception):
    def __str__(self) -> str:
        return f"Y coordinate is out of range"

class SudokuGrid():
    def __init__(self, rows: list[list], block_size: int):
        grid_width = len(rows[0])

        if len(rows) % block_size != 0:
            raise SudokuGridBlockError

        for row in rows:
            if len(row) != grid_width:
                raise SudokuGridRowError

            if len(row) % block_size != 0:
                raise SudokuGridBlockError
        
        self.rows = rows
        self.grid_width = grid_width
        self.grid_height = len(self.rows)
        self.block_size = block_size

    def get_column(self, x:int):
        if x+1 > self.grid_width:
            raise SudokuGridXOutOfRange

        return [row[x] for row in self.rows]

    def get_block(self, x:int, y:int):
        if x+1 > self.grid_width:
            raise SudokuGridXOutOfRange
        if y+1 > self.grid_height:
            raise SudokuGridYOutOfRange

        results = []
        x_min = ((x // self.block_size) * self.block_size)
        x_max = x_min + self.block_size -1
        y_min = ((y // self.block_size) * self.block_size)
        y_max = y_min + self.block_size -1

        for i, row in enumerate(self.rows):
            for j, col in enumerate(row):
                if x_min <= j <= x_max and y_min <= i <= y_max:
                    results.append(col)

        return results



