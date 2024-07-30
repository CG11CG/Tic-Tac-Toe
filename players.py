def validate_move(board, move):
    row, col = move
    if 0 <= row < 3 and 0 <= col < 3:
        return board[row][col] == " "
    return False

def switch_player(current_player):
    return "O" if current_player == "X" else "X"

def get_move():
    while True:
        try:
            move = input("Enter your move (row and column): ")
            row, col = map(int, move.split())
            if 0 <= row < 3 and 0 <= col < 3:
                return (row, col)
            else: 
                print("Move out of bounds. Try again")
        except ValueError:
            print("Invalid input. Enter two numbers separated by a space.")
