# 2048-Game-with-Python
 The application is an implementation of the game 2048 using Tkinter, a graphical Python module. It creates a graphical interface where the user can move the numbered tiles using the arrow keys. The goal of the game is to combine the tiles until the value 2048 is obtained.

Tkinter is used to create the graphical interface.
Random is used to place new tiles on the board.


• The Game2048 (Game Initialization):
  
The main class that manages the game logic and interface.

Creates a main window for the game.

Binds keyboard events to the handle_key function, which detects arrow presses.

The game board is represented by a 4x4 matrix filled with 0's.

The score starts from 0.


 
• Creating the graphical interface - def init_grid(self):

This function visually creates a 4x4 grid using Label from Tkinter.

A Label is created for each cell.

It is saved in a two-dimensional list self.tiles.


• Add a new tile (2 or 4) - def add_tile(self):

This function randomly chooses an empty cell and adds a new tile.

Creates a list of all empty cells (with value 0).

Selects a random cell and assigns it 2 (90% chance) or 4 (10% chance).


 
• Update the display - def update_grid(self):

This function updates the values in the interface.

If the cell is empty, it colors it gray.

If the cell has a value, it displays the number and colors it light blue.


• Detect keys and move pieces - def handle_key(self, event):

This function handles moving the tiles when the user presses the arrow keys.

It moves the tiles and adds a new tile with each move.

If no more moves are possible, displays the message "Game Over".


• Move logic - def move_tiles(self, direction):

This function moves and combines tiles in the desired direction.

Up: Uses transpose to move the tiles as if they were rows.

Down: This is similar to Up, but also includes row reversal.

Left moves and combines normally.

Right reverses rows, moves, then reverses back.


• Check game over - def check_game_over(self):

This function checks for possible moves.

If there are no more possible moves, the game ends.


• Starting the game - def main():

Creates the window and starts the game.
