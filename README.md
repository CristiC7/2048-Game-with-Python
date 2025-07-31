# 🎮 2048 Game with Python (Tkinter)

This project is a clean and functional implementation of the classic **2048 game**, built entirely with **Python** and the **Tkinter** GUI module.

The objective of the game is simple: **combine tiles** by moving them with arrow keys until you reach the **2048** tile.

---

## 📦 Technologies Used

- `tkinter` – For graphical user interface (GUI)
- `random` – For generating new tiles (2 or 4)

---

## 🚀 How It Works

### 🧱 Class: `Game2048`

The main class that handles both the game logic and interface.

✅ Creates the game window

✅ Initializes a 4x4 matrix (`grid`) filled with 0s

✅ Sets the initial score to 0

✅ Binds arrow key presses (`↑ ↓ ← →`) to tile movement

---

## 🎮 Key Functions

### 📊 `init_grid(self)`

- Creates the **visual grid** using Tkinter `Label` widgets
- Stores the GUI tiles in `self.tiles` as a 2D list

---

### 🎲 `add_tile(self)`

- Identifies all empty cells (`value == 0`)
- Randomly places a new tile (90% chance of 2, 10% chance of 4)

---

### 🔁 `update_grid(self)`

- Updates the GUI based on the matrix (`self.grid`)
- Colors:
  - Empty = gray
  - Tile = light blue with number

---

### 🎯 `handle_key(self, event)`

- Handles arrow key input
- Triggers `move_tiles()`
- Adds a new tile after each valid move
- Checks for game over

---

### 🔄 `move_tiles(self, direction)`

- Logic for merging tiles:
  - `Up`: Transpose → Merge → Transpose back
  - `Down`: Transpose + Reverse → Merge → Reverse + Transpose back
  - `Left`: Merge directly
  - `Right`: Reverse → Merge → Reverse back

---

### ❌ `check_game_over(self)`

- Verifies if there are no moves left:
  - No empty cells
  - No adjacent equal tiles (horizontal or vertical)
- If true: prints `"Game Over!"` with final score

---

### 🧠 Utilities

- `transpose(matrix)`: Swaps rows and columns
- `reverse(matrix)`: Reverses each row

---

## ▶️ How to Run

Save the file as `2048.py` and run:

```bash
python 2048.py
```

---

## ⌨️ Controls
⬆️ Up Arrow – Move tiles up

⬇️ Down Arrow – Move tiles down

⬅️ Left Arrow – Move tiles left

➡️ Right Arrow – Move tiles right

---

## 🔧 Possible Improvements
- Add color variation based on tile value

- Display current score and high score in the window

- Add restart/new game button

- Use a popup for Game Over instead of printing to console

- Add animations for smoother transitions

---

## 👤 Author
Created by CristiC7

Focused on clean Python GUI projects with classic game logic.

Feel free to fork, customize, or contribute!
