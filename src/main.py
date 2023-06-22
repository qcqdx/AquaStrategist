"""
AquaStrategist: Battleship Game

This file contains the main GUI for the AquaStrategist game. The GUI includes
two sections representing the player's and AI's game boards, and a status section
for displaying the game state, such as score and messages.

Author: qcqdx
License: MIT License
"""

import tkinter as tk


def draw_grid(canvas, rows, cols, cell_size):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(rows + 1):
        canvas.create_line((i + 1) * cell_size, cell_size, (i + 1) * cell_size, cell_size * (rows + 1))
        if i < rows:
            canvas.create_text((i + 1.5) * cell_size, cell_size / 2, text=letters[i], anchor="center")
    for j in range(cols + 1):
        canvas.create_line(cell_size, (j + 1) * cell_size, cell_size * (cols + 1), (j + 1) * cell_size)
        if j < cols:
            canvas.create_text(cell_size / 2, (j + 1.5) * cell_size, text=str(j + 1), anchor="center")


# Create the main window
root = tk.Tk()
root.title("AquaStrategist - Battleship")
root.geometry("900x400")

# Create frames to section the window
player_frame = tk.Frame(root, width=300, height=300, bg="lightblue")
ai_frame = tk.Frame(root, width=300, height=300, bg="lightcoral")
status_frame = tk.Frame(root, width=600, height=100, bg="lightgray")

# Place the frames in the window
player_frame.pack(side="left", padx=20, pady=20)
ai_frame.pack(side="left", padx=20, pady=20)
status_frame.pack(side="bottom", padx=20, pady=20, fill="x")

# Create canvases within the respective frames for the game boards
player_canvas = tk.Canvas(player_frame, width=220, height=220, bg="white")
ai_canvas = tk.Canvas(ai_frame, width=220, height=220, bg="white")

# Place the canvases within the frames
player_canvas.pack(padx=20, pady=20)
ai_canvas.pack(padx=20, pady=20)

# Draw grids on the canvases
draw_grid(player_canvas, 10, 10, 20)
draw_grid(ai_canvas, 10, 10, 20)

# Create a label within the status frame for displaying game status
status_label = tk.Label(status_frame, text="Preparing Game", bg="lightgray", font=("Arial", 16))
status_label.pack(pady=20)


class Ship:
    def __init__(self, size, x, y, orientation):
        self.size = size
        self.x = x
        self.y = y
        self.orientation = orientation  # 'horizontal' or 'vertical'
        self.placed = False

    def draw(self, canvas, cell_size):
        if self.placed:
            color = "darkgray"
        else:
            color = "green"  # Will need logic to check if placement is valid

        if self.orientation == 'horizontal':
            x1 = self.x * cell_size
            y1 = self.y * cell_size
            x2 = x1 + (self.size * cell_size)
            y2 = y1 + cell_size
        else:  # vertical
            x1 = self.x * cell_size
            y1 = self.y * cell_size
            x2 = x1 + cell_size
            y2 = y1 + (self.size * cell_size)

        canvas.create_rectangle(x1, y1, x2, y2, fill=color)


# Create a ship
my_ship = Ship(size=3, x=2, y=2, orientation='horizontal')

# Draw the ship on the player's canvas
my_ship.draw(player_canvas, 20)

# Start the main loop
root.mainloop()
