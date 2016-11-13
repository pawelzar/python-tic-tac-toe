class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.n = len(board[0])

    def is_correct(self):
        """
        Return True if board is NxN and False if not.
        """
        for row in self.board:
            if len(row) != self.n:
                return False
        return True

    def check_rows(self):
        """
        Return 'X' if any row consists entirely of 'X', 'O' accordingly.
        If there is no such row, then return '.'.
        """
        for row in self.board:
            if all(a == 'X' for a in row):
                return 'X'
            elif all(a == 'O' for a in row):
                return 'O'
        return '.'

    def check_columns(self):
        """
        Return 'X' if any column consists entirely of 'X', 'O' accordingly.
        If there is no such column, then return '.'.
        """
        count_x, count_o = 0, 0
        for i in range(self.n):
            for j in range(self.n):
                count_x += int(self.board[j][i] == 'X')
                count_o += int(self.board[j][i] == 'O')
            if count_x == self.n:
                return 'X'
            elif count_o == self.n:
                return 'O'
            count_x, count_o = 0, 0
        return '.'

    def check_diagonals(self):
        """
        Return 'X' if any diagonal consists entirely of 'X', 'O' accordingly.
        Otherwise return '.'.
        """
        count_x, count_o = 0, 0
        count_anti_x, count_anti_o = 0, 0
        for i in range(self.n):
            count_x += int(self.board[i][i] == 'X')
            count_o += int(self.board[i][i] == 'O')
            count_anti_x += int(self.board[i][self.n-i-1] == 'X')
            count_anti_o += int(self.board[i][self.n-i-1] == 'O')
        if count_x == self.n or count_anti_x == self.n:
            return 'X'
        elif count_o == self.n or count_anti_o == self.n:
            return 'O'
        else:
            return '.'

    def check_winner(self):
        """
        Return winner by checking all possibilities.
        A player has won if occupies an entire row, column or diagonal.
        """
        winner = "."
        possibilities = [
            self.check_rows,
            self.check_columns,
            self.check_diagonals,
        ]

        while winner == '.' and possibilities:
            winner = possibilities[0]()
            del possibilities[0]

        return winner


if __name__ == "__main__":
    first_row = input()
    game = TicTacToe([first_row])

    while len(game.board) < game.n:
        game.board.append(input())

    if not game.is_correct():
        exit(1)
    else:
        print(game.check_winner())
