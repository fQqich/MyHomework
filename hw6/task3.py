from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    # check rows
    for row in board:
        if row.count('x') == 3:
            return 'x wins!'
        elif row.count('o') == 3:
            return 'o wins!'

    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'x':
                return 'x wins!'
            elif board[0][i] == 'o':
                return 'o wins!'

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'x':
            return 'x wins!'
        elif board[0][0] == 'o':
            return 'o wins!'
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'x':
            return 'x wins!'
        elif board[0][2] == 'o':
            return 'o wins!'

    # check if unfinished or draw
    for row in board:
        if '.' in row:
            return 'unfinished!'
    return 'draw!'