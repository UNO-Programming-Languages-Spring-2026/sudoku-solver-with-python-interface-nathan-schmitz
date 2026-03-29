import sys, clingo
from sudoku_board import Sudoku

class Context:

    def __init__(self, board: Sudoku):
        self.board = board
        
    def initial(self) -> list[clingo.symbol.Symbol]:
        symbols = []
        for (row, column), value in self.board.sudoku.items():
            symbols.append( clingo.Tuple_((clingo.Number(row), clingo.Number(column), clingo.Number(value))) )
        return symbols

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")
        
        for file in files:
            with open(file, 'r') as f:
                context = Context(Sudoku.from_str(f.read()))
        
        ctl.ground(context=context)
        ctl.solve()
    
    def print_model(self, model, printer) -> None:
        board = Sudoku.from_model(model)
        print(board)
        sys.stdout.flush()
        

clingo.application.clingo_main(ClingoApp())