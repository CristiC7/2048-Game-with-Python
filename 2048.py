import tkinter as tk  # Importing tkinter for GUI
import random  # Importing random for tile placement

class Game2048:
    def __init__(self, master):
        # Initialize the main game window
        self.master = master
        self.master.title("2048")  # Set window title
        self.master.geometry("400x400")  # Set window size
        self.master.bind("<Key>", self.handle_key)  # Bind keyboard events

        self.grid_size = 4  # Define the grid size (4x4)
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]  # Initialize the grid with zeros
        self.score = 0  # Initialize the score

        self.init_grid()  # Create the graphical grid
        self.add_tile()  # Add the first random tile
        self.update_grid()  # Update the grid display

    def init_grid(self):
        # Create the 4x4 grid using Tkinter labels
        self.tiles = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                tile = tk.Label(self.master, text="", font=("Helvetica", 32), width=4, height=2, relief="raised")
                tile.grid(row=i, column=j, padx=5, pady=5)  # Place the tile in the grid
                row.append(tile)
            self.tiles.append(row)

    def add_tile(self):
        # Add a new tile (2 or 4) to a random empty position
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)  # Pick a random empty cell
            self.grid[i][j] = 2 if random.random() < 0.9 else 4  # 90% chance of getting 2, 10% chance of getting 4

    def update_grid(self):
        # Update the grid display based on the current values
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid[i][j]
                if value == 0:
                    self.tiles[i][j].configure(text="", bg="lightgray")  # Empty cell
                else:
                    self.tiles[i][j].configure(text=str(value), bg="lightblue")  # Tile with a number
        self.master.update_idletasks()  # Refresh the window

    def handle_key(self, event):
        # Handle keyboard input for movement
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.move_tiles(event.keysym)  # Move tiles in the specified direction
            self.add_tile()  # Add a new tile after a move
            self.update_grid()  # Update the display
            if self.check_game_over():  # Check if the game is over
                print("Game Over! Score:", self.score)

    def move_tiles(self, direction):
        # Move tiles in the specified direction
        if direction == 'Up':
            self.grid = self.transpose(self.grid)  # Convert columns into rows
            self.grid = self.merge_tiles(self.grid)  # Merge tiles
            self.grid = self.transpose(self.grid)  # Convert back
        elif direction == 'Down':
            self.grid = self.reverse(self.transpose(self.grid))  # Flip and transpose
            self.grid = self.merge_tiles(self.grid)
            self.grid = self.transpose(self.reverse(self.grid))  # Flip and transpose back
        elif direction == 'Left':
            self.grid = self.merge_tiles(self.grid)  # Merge normally
        elif direction == 'Right':
            self.grid = self.reverse(self.grid)  # Reverse the rows
            self.grid = self.merge_tiles(self.grid)
            self.grid = self.reverse(self.grid)  # Reverse back

    def merge_tiles(self, grid):
        # Merge adjacent tiles of the same value
        score = 0
        for i in range(self.grid_size):
            j = 0
            while j < self.grid_size - 1:
                if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                    grid[i][j] *= 2  # Merge tiles by doubling the value
                    score += grid[i][j]  # Update the score
                    grid[i][j+1] = 0  # Clear the merged tile
                    j += 2  # Skip the next tile to avoid double merging
                else:
                    j += 1
        self.score += score  # Update total score
        return grid

    def check_game_over(self):
        # Check if there are no possible moves left
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 0:
                    return False  # Game is not over if there is an empty cell
                if j < self.grid_size - 1 and self.grid[i][j] == self.grid[i][j+1]:
                    return False  # Game is not over if adjacent horizontal tiles can merge
                if i < self.grid_size - 1 and self.grid[i][j] == self.grid[i+1][j]:
                    return False  # Game is not over if adjacent vertical tiles can merge
        return True  # No moves left, game over

    @staticmethod
    def transpose(matrix):
        # Transpose a matrix (swap rows and columns)
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    @staticmethod
    def reverse(matrix):
        # Reverse the order of elements in each row
        return [row[::-1] for row in matrix]

def main():
    # Initialize the game window
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()  # Run the game
