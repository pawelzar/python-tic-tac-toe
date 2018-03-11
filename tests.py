from unittest import TestCase

from tictactoe import TicTacToe


class BoardTestCase(TestCase):
    def test_correct_board(self):
        board = [
            '...',
            '...',
            '...',
        ]
        game = TicTacToe(board)
        self.assertTrue(game.is_correct(),
                        'Should return True if board is square.')

    def test_incorrect_board(self):
        board = [
            'XXOO.',
            '...X.',
            'OOOO',
            '..',
            '.....',
        ]
        game = TicTacToe(board)
        self.assertFalse(game.is_correct(),
                         'Should return False if board is not square.')


class WinnerTestCase(TestCase):
    def test_3x3_no_winner(self):
        board = [
            'XO.',
            '.Ox',
            '.X.',
        ]
        game = TicTacToe(board)
        self.assertEqual('.', game.result(),
                         'Should not return any winner.')

    def test_4x4_row(self):
        board = [
            'XXX.',
            'X...',
            '.OOO',
            '....',
        ]
        game = TicTacToe(board)
        self.assertIsNone(game.check_rows(),
                         'Should not win if row is incomplete.')

        game.board = [
            'X...',
            '....',
            'OOOO',
            'X...',
        ]
        self.assertEqual('O', game.check_rows(),
                         'Should win if row is complete.')

        game.board = [
            'X...',
            '....',
            'XXXX',
            'X...',
        ]
        self.assertEqual('X', game.check_rows(),
                         'Should win if row is complete.')

    def test_4x4_column(self):
        board = [
            'X...',
            'X...',
            'X...',
            '....',
        ]
        game = TicTacToe(board)
        self.assertIsNone(game.check_columns(),
                         'Should not win if column is incomplete.')

        game.board = [
            'X...',
            'X...',
            'X...',
            'X...',
        ]
        self.assertEqual('X', game.check_columns(),
                         'Should win if column is complete.')

    def test_4x4_diagonal(self):
        board = [
            'X...',
            '.X..',
            '..X.',
            '....',
        ]
        game = TicTacToe(board)
        self.assertIsNone(game.check_diagonals(),
                         'Should not win if diagonal is incomplete.')

        game.board = [
            'X...',
            '.X..',
            '..X.',
            '...X',
        ]
        self.assertEqual('X', game.check_diagonals(),
                         'Should win if diagonal is complete.')

    def test_4x4_anti_diagonal(self):
        board = [
            '...X',
            '..X.',
            '.X..',
            '....',
        ]
        game = TicTacToe(board)
        self.assertIsNone(game.check_diagonals(),
                         'Should not win if diagonal is incomplete.')

        game.board = [
            '...O',
            '..O.',
            '.O..',
            'O...',
        ]
        self.assertEqual('O', game.check_diagonals(),
                         'Should win if diagonal is complete.')


class FullTestCase(TestCase):
    def setUp(self):
        board = [
            'XOXOXO',
            'O..O.X',
            '.XXO..',
            'OOXO.O',
            'X.XO.X',
            '..XOX.',
        ]
        self.game = TicTacToe(board)

    def test_all_in_one(self):
        self.assertIsNone(self.game.check_rows(),
                         'Should not detect complete row.')
        self.assertIsNone(self.game.check_diagonals(),
                         'Should not detect complete diagonal.')
        self.assertEqual('O', self.game.check_columns(),
                         'Should detect complete column.')
        self.assertEqual('O', self.game.result(),
                         'Should win if column is complete.')
