# Tic-tac-toe win state checker

The rules of a Tic-tac-toe (https://en.wikipedia.org/wiki/Tictactoe):
- Played on an NxN board.
- Two players, X and O.
- A player has won if occupies an entire row, column or diagonal.

The program should accept a board state through stdin, and output a "X" or "O" if either of those
players won, and "." if no player has won. If the state of the board is invalid, the program should fail
(exit with a nonzero
exit code). If both players won, either "X" or "O" are acceptable outputs.
You should expect input of the form:
```
XO.
.Ox
.X.
```
Where "." indicates an unoccupied place on the playing board.
For the above example, you should output ".".
