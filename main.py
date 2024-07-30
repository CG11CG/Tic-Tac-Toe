def check_win(board):
    #Checks rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    #Checks Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    #Check Diagonals
    if board[0][0] == board[1][1] == board [2][2] != " ":
        return True
    
    if board[0][2] == board[1][1] == board [2][0] != " ":
        return True
    
    return False

def check_draw(board):
    pass

def play_turn(board, player):
    pass

def main():