class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.size = len(board[0])
        self.no_winner = '.'

    def is_correct(self):
        """
        Check if board is square.
        """
        return not any(len(row) != self.size for row in self.board)

    def check_rows(self):
        """
        Check if any player occupies any row entirely.

        :return: indicator of player that occupies the entire row
        """
        for row in self.board:
            if all(a == 'X' for a in row):
                return 'X'
            elif all(a == 'O' for a in row):
                return 'O'

        return self.no_winner

    def check_columns(self):
        """
        Check if any player occupies any column entirely.

        :return: indicator of player that occupies the entire column
        """
        for col in zip(*self.board):
            if all(a == 'X' for a in col):
                return 'X'
            elif all(a == 'O' for a in col):
                return 'O'

        return self.no_winner

    def check_diagonals(self):
        """
        Check if any player occupies any diagonal entirely.

        :return: indicator of player that occupies the entire diagonal
        """
        count_x, count_anti_x = 0, 0
        count_o, count_anti_o = 0, 0

        for i in range(self.size):
            count_x += int(self.board[i][i] == 'X')
            count_o += int(self.board[i][i] == 'O')
            count_anti_x += int(self.board[i][self.size - i - 1] == 'X')
            count_anti_o += int(self.board[i][self.size - i - 1] == 'O')

        if count_x == self.size or count_anti_x == self.size:
            return 'X'
        elif count_o == self.size or count_anti_o == self.size:
            return 'O'

        return self.no_winner

    def result(self):
        """
        Check which player won the game. A player has won if occupies
        an entire row, column or diagonal.

        :return: indicator of player that won the game
        """
        possibilities = [
            self.check_rows, self.check_columns, self.check_diagonals
        ]

        for possibility in possibilities:
            result = possibility()
            if result != self.no_winner:
                return result

        return self.no_winner


if __name__ == '__main__':
    FIRST_ROW = input()
    GAME = TicTacToe([FIRST_ROW])

    while len(GAME.board) < GAME.size:
        GAME.board.append(input())

    if not GAME.is_correct():
        exit(1)

    print(GAME.result())
