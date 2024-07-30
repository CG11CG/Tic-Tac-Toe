from board import initialize_board, print_board, update_board, check_win, check_draw
from players import validate_move, switch_player, get_move

def main():
    board = initialize_board()
    current_player = "X"
    
    while True:
        print_board(board)
        move = get_move()
        
        if validate_move(board, move):
            update_board(board, move, current_player)
            
            if check_win(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            
            current_player = switch_player(current_player)
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()