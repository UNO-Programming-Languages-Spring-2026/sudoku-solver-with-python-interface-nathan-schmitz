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

        # Counters to keep track of the location in the dictionary (originally used enumerate() but the boxes through that off)
        current_row = 1
        current_column = 1

        # Iterate through each line of the string
        for row in s.split('\n'):
            # If the line is empty, move on without incrementing current_row
            if row == '':
                continue
            
            # Iterate through all cells in the row
            for value in row.split(' '):
                # If there is nothing between spaces, move on without increment current_column
                if value == '':
                    continue
                
                # If there is a value, add it to the dictionary
                if value != '-':
                    sudoku[current_row, current_column] = int(value)

                # Increment the column
                current_column += 1
            
            # Reset the column, and increment the row
            current_column = 1
            current_row += 1

        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for symbol in model.symbols(shown=True):
            row, column, value = symbol.arguments
            sudoku[row.number, column.number] = value.number
        return cls(sudoku)
