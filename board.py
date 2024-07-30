def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print("-" * 9)

def update_board(board, move, player):
    row, col = move
    board[row][col] = player

def check_win(board):
    # Checks rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    # Checks columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    # Checks diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

