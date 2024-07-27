def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in (board):
        print(' | '.join(row))
        print("-" * 5)

def update_board(board, move, player):
    pass
