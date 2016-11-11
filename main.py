def check_row(row):
    if all(x == 'X' for x in row):
        return 'X'
    elif all(x == 'O' for x in row):
        return 'O'
    else:
        return '.'


def check_diagonal(board):
    n = len(board)
    count_x = 0
    count_o = 0
    for i in range(n):
        for j in range(n):
            count_x += int(board[i][j] == 'X')
            count_o += int(board[i][j] == 'O')
    if count_x == n:
        return 'X'
    elif count_o == n:
        return 'O'
    else:
        return '.'


def check_anti_diagonal(board):
    pass


def check_all_columns(board):
    n = len(board)
    count_x = 0
    count_o = 0
    for i in range(n):
        for j in range(n):
            count_x += int(board[j][i] == 'X')
            count_o += int(board[j][i] == 'O')
        if count_x == n:
            return 'X'
        elif count_o == n:
            return 'O'
    return '.'


first_row = input()
n = len(first_row)
board = [first_row]

while len(board) < n:
    row = input()
    if len(row) != n:
        exit(1)
    elif check_row(row) != '.':
        print(check_row(row))
    else:
        board.append(row)
