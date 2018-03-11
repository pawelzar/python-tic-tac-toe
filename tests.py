from unittest import TestCase

from tictactoe import TicTacToe


class TicTacToeBoardTestCase(TestCase):
    def test_correct_board_should_return_true_if_board_is_square(self):
        game = TicTacToe([
            '...',
            '...',
            '...',
        ])
        self.assertTrue(game.is_correct())

    def test_correct_board_should_return_false_if_board_is_not_square(self):
        game = TicTacToe([
            'XXOO.',
            '...X.',
            'OOOO',
            '..',
            '.....',
        ])
        self.assertFalse(game.is_correct())


class TicTacToeWinnerTestCase(TestCase):
    def test_check_rows_should_return_none_if_row_is_incomplete(self):
        game = TicTacToe([
            'XXX.',
            'X...',
            '.OOO',
            '....',
        ])
        self.assertIsNone(game.check_rows())

    def test_check_rows_should_return_winner_if_row_is_complete(self):
        game = TicTacToe([
            'X...',
            '....',
            'OOOO',
            'X...',
        ])
        self.assertEqual('O', game.check_rows())

        game = TicTacToe([
            'X...',
            '....',
            'XXXX',
            'X...',
        ])
        self.assertEqual('X', game.check_rows())

    def test_check_columns_should_return_none_if_column_is_incomplete(self):
        game = TicTacToe([
            'X...',
            'X...',
            'X...',
            '....',
        ])
        self.assertIsNone(game.check_columns())

    def test_check_columns_should_return_winner_if_column_is_complete(self):
        game = TicTacToe([
            'X...',
            'X...',
            'X...',
            'X...',
        ])
        self.assertEqual('X', game.check_columns())

        game = TicTacToe([
            'O...',
            'O...',
            'O...',
            'O...',
        ])
        self.assertEqual('O', game.check_columns())

    def test_check_diagonals_should_return_none_if_diagonal_is_incomplete(self):
        game = TicTacToe([
            'X...',
            '.X..',
            '..X.',
            '....',
        ])
        self.assertIsNone(game.check_diagonals())

        game = TicTacToe([
            '...X',
            '..X.',
            '.X..',
            '....',
        ])
        self.assertIsNone(game.check_diagonals())


    def test_check_diagonals_should_return_winner_if_diagonal_is_complete(self):
        game = TicTacToe([
            'X...',
            '.X..',
            '..X.',
            '...X',
        ])
        self.assertEqual('X', game.check_diagonals())

        game = TicTacToe([
            '...O',
            '..O.',
            '.O..',
            'O...',
        ])
        self.assertEqual('O', game.check_diagonals())

    def test_result_should_return_dot_if_no_winner(self):
        game = TicTacToe([
            'XO.',
            '.Ox',
            '.X.',
        ])
        self.assertEqual('.', game.result())

    def test_result_should_return_winner_if_row_is_complete(self):
        game = TicTacToe([
            'XXX',
            '.Ox',
            '.X.',
        ])
        self.assertEqual('X', game.result())


class TicTacToeComprehensiveTestCase(TestCase):
    def setUp(self):
        self.game = TicTacToe([
            'XOXOXO',
            'O..O.X',
            '.XXO..',
            'OOXO.O',
            'X.XO.X',
            '..XOX.',
        ])

    def test_board_should_be_correct(self):
        self.assertTrue(self.game.is_correct())

    def test_should_not_detect_complete_row(self):
        self.assertIsNone(self.game.check_rows())

    def test_should_not_detect_complete_diagonal(self):
        self.assertIsNone(self.game.check_diagonals())

    def test_should_detect_complete_column(self):
        self.assertEqual('O', self.game.check_columns())

    def test_should_return_winner_based_on_complete_column(self):
        self.assertEqual('O', self.game.result())
