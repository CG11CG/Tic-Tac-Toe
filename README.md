Tic Tac Toe Game

Description
This is a simple Tic Tac Toe game implemented in Python. The game allows two players to play against each other on a 3x3 grid. Players take turns to place their respective marks (X or O) on the board. The game ends when one player gets three of their marks in a row, column, or diagonal, or when the board is full resulting in a draw.

Features
Two-player mode
3x3 grid game board
Simple text-based interface
Input validation for moves
Automatic detection of win and draw conditions

Files
board.py: Contains functions related to the game board such as initializing, printing, and updating the board.
game.py: Contains functions for checking win and draw conditions, playing turns, and the main game loop.
players.py: Contains functions for validating moves, switching players, and getting player moves.

How to Run
Ensure you have Python installed on your system.
Clone the repository to your local machine.
Navigate to the directory containing the game files.
Run the players.py file using Python:
bash
Copy code
python players.py

Usage
The game starts by initializing a 3x3 board.
Players take turns to enter their moves.
The game checks for win or draw conditions after each move.
The game continues until there is a winner or the board is full resulting in a draw.
Functions

board.py
initialize_board(): Initializes and returns a 3x3 game board.
print_board(board): Prints the current state of the game board.
update_board(board, move, player): Updates the game board with the player's move.

game.py
check_win(board): Checks if there is a winner on the board.
check_draw(board): Checks if the game is a draw.
play_turn(board, current_player): Handles a player's turn, including getting the move and updating the board.
main(): The main game loop that runs the Tic Tac Toe game.

players.py
validate_move(board, move): Validates if a move is legal.
switch_player(current_player): Switches the current player.
get_move(): Gets a move from the current player.
