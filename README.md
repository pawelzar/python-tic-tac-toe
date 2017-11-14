# Tic-tac-toe win state checker
[![Build Status](https://travis-ci.org/pawelzar/python-tic-tac-toe.svg?branch=master)](https://travis-ci.org/pawelzar/python-tic-tac-toe)
[![Coverage Status](https://codecov.io/gh/pawelzar/python-tic-tac-toe/branch/master/graph/badge.svg)](https://codecov.io/gh/pawelzar/python-tic-tac-toe)
[![Code Quality](https://codebeat.co/badges/088ff987-55ed-4722-a472-52fd2233b262)](https://codebeat.co/projects/github-com-pawelzar-python-tic-tac-toe-master)

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
