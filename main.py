class TicTacToe:
    @staticmethod
    def board_is_correct(board):
        n = len(board)
        for row in board:
            if len(row) != n:
                return False
        return True

    @staticmethod
    def check_all_rows(board):
        for row in board:
            if all(a == 'X' for a in row):
                return 'X'
            elif all(a == 'O' for a in row):
                return 'O'
        else:
            return '.'

    @staticmethod
    def check_all_columns(board):
        n = len(board)
        count_x, count_o = 0, 0
        for i in range(n):
            for j in range(n):
                count_x += int(board[j][i] == 'X')
                count_o += int(board[j][i] == 'O')
            if count_x == n:
                return 'X'
            elif count_o == n:
                return 'O'
            count_x, count_o = 0, 0
        return '.'

    @staticmethod
    def check_diagonal(board):
        n = len(board)
        count_x, count_o = 0, 0
        for i in range(n):
            count_x += int(board[i][i] == 'X')
            count_o += int(board[i][i] == 'O')
        if count_x == n:
            return 'X'
        elif count_o == n:
            return 'O'
        else:
            return '.'

    @staticmethod
    def check_anti_diagonal(board):
        n = len(board)
        count_x, count_o = 0, 0
        for i in range(n-1, -1, -1):
            count_x += int(board[i][i] == 'X')
            count_o += int(board[i][i] == 'O')
        if count_x == n:
            return 'X'
        elif count_o == n:
            return 'O'
        else:
            return '.'

    @staticmethod
    def check_winner(board):
        """Return winner by checking all conditions."""
        winner = TicTacToe.check_all_rows(board)
        possibilities = [
            TicTacToe.check_all_columns,
            TicTacToe.check_diagonal,
            TicTacToe.check_anti_diagonal
        ]

        while winner == '.' and possibilities:
            winner = possibilities[0](board)
            del possibilities[0]

        return winner


if __name__ == "__main__":
    first_row = input()
    n = len(first_row)
    board = [first_row]

    while len(board) < n:
        board.append(input())

    if not TicTacToe.board_is_correct(board):
        exit(1)
    else:
        print(TicTacToe.check_winner(board))
