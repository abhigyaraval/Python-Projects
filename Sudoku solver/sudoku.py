# Sudoku solver >> sudoku.py--- Contains the sudoku class
# Author: Abhigya Raval

class sudoku:
    def __int__(self, x, y, grid):
        self.pos = [x, y]
        self.val = grid[x, y]
