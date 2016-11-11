import unittest
from main import TicTacToe as Tic


class Test(unittest.TestCase):
    def test_3x3_no_winner(self):
        board = [
            'XO.',
            '.Ox',
            '.X.'
        ]
        self.assertEqual(".", Tic.check_whole_board(board))

    def test_4x4_win(self):
        board = [
            'X...',
            '.X..',
            '..X.',
            '...X'
        ]
        self.assertEqual("X", Tic.check_whole_board(board))
