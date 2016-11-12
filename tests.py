import unittest
from tictactoe import TicTacToe as Tic


class BoardTestCase(unittest.TestCase):
    def test_correct_board(self):
        board = [
            '...',
            '...',
            '...'
        ]
        self.assertTrue(Tic.board_is_correct(board),
                        "Should return True if board is NxN.")

    def test_incorrect_board(self):
        board = [
            'XXOO.',
            '...X.',
            'OOOO',
            '....',
            '.....'
        ]
        self.assertFalse(Tic.board_is_correct(board),
                         "Should return False if board is not NxN.")


class WinnerTestCase(unittest.TestCase):
    def test_3x3_no_winner(self):
        board = [
            'XO.',
            '.Ox',
            '.X.'
        ]
        self.assertEqual(".", Tic.check_winner(board),
                         "Should not be any winner.")

    def test_4x4_row(self):
        board = [
            'XXX.',
            'X...',
            '.OOO',
            '....'
        ]
        self.assertEqual('.', Tic.check_all_rows(board),
                         "Should not win if row is incomplete.")

        board = [
            'X...',
            '....',
            'OOOO',
            'X...'
        ]
        self.assertEqual('O', Tic.check_all_rows(board),
                         "Should win if row is complete.")

    def test_4x4_column(self):
        board = [
            'X...',
            'X...',
            'X...',
            '....'
        ]
        self.assertEqual('.', Tic.check_all_columns(board),
                         "Should not win if column is incomplete.")

        board = [
            'X...',
            'X...',
            'X...',
            'X...'
        ]
        self.assertEqual('X', Tic.check_all_columns(board),
                         "Should win if column is complete.")

    def test_4x4_diagonal(self):
        board = [
            'X...',
            '.X..',
            '..X.',
            '....'
        ]
        self.assertEqual('.', Tic.check_diagonal(board),
                         "Should not win if diagonal is incomplete.")

        board = [
            'X...',
            '.X..',
            '..X.',
            '...X'
        ]
        self.assertEqual("X", Tic.check_diagonal(board),
                         "Should win if diagonal is complete.")

    def test_4x4_anti_diagonal(self):
        board = [
            '...X',
            '..X.',
            '.X..',
            '....'
        ]
        self.assertEqual('.', Tic.check_anti_diagonal(board),
                         "Should not win if diagonal is incomplete.")

        board = [
            '...O',
            '..O.',
            '.O..',
            'O...'
        ]
        self.assertEqual("O", Tic.check_anti_diagonal(board),
                         "Should win if diagonal is complete.")
