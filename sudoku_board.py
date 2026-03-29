from typing import Tuple
import clingo

class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # Iterate through all cells
        for i in range(1, 10):
            for j in range(1, 10):
                # Add the number in that cell
                s += str(self.sudoku[(i, j)]) + ' '

                # Add the space for the box
                if j == 3 or j == 6:
                    s += ' '
            
            # Add an empty line for box
            if i == 3 or i == 6:
                s += '\n'
            
            # Start new row
            s += '\n'
        
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for symbol in model.symbols(shown=True):
            row, column, value = symbol.arguments
            sudoku[row.number, column.number] = value.number
        return cls(sudoku)
