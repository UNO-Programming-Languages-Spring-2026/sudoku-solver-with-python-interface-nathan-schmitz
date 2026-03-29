% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

{ sudoku(X, Y, N) : N = 1..9 } = 1 :- X = 1..9, Y = 1..9.
% Acheived: Every cell has a number from 1 to 9

subgrid(X, Y, G) :- G == (((Y - 1) \ 9) / 3 + 1) + 3 * ((X - 1) / 3), G = 1..9, Y = 1..9, X = 1..9.
% Acheived: subgrids assigned to the proper corners of the grid

:- initial(X, Y, N), not sudoku(X, Y, N).
% Acheived: Removed solutions that do not match the intial board

:- sudoku(X, Y1, N), sudoku(X, Y2, N), Y1 != Y2.
% Acheived: Removed solutions where the same number is in the same row, but different columns

:- sudoku(X1, Y, N), sudoku(X2, Y, N), X1 != X2.
% Acheived: Removed solutions where the same number is in the same column, but different rows

:- sudoku(X1, Y1, N), sudoku(X2, Y2, N), X1 != X2, Y1 != Y2, subgrid(X1, Y1, G), subgrid(X2, Y2, G).
% Achieved: Removed solutions where the same number is in the same subgrid as itself

#show sudoku/3.