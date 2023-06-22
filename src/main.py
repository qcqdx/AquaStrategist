"""
AquaStrategist: Battleship Game

This file contains the main GUI for the AquaStrategist game. The GUI includes
two sections representing the player's and AI's game boards, and a status section
for displaying the game state, such as score and messages.

Author: qcqdx
License: MIT License
"""

import tkinter as tk

# Function to draw a grid on a canvas
def draw_grid(canvas, rows, cols, cell_size):
    for i in range(rows + 1):
        canvas.create_line(i * cell_size, 0, i * cell_size, cell_size * rows)
    for j in range(cols + 1):
        canvas.create_line(0, j * cell_size, cell_size * cols, j * cell_size)

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
player_canvas = tk.Canvas(player_frame, width=200, height=200, bg="white")
ai_canvas = tk.Canvas(ai_frame, width=200, height=200, bg="white")

# Place the canvases within the frames
player_canvas.pack(padx=20, pady=20)
ai_canvas.pack(padx=20, pady=20)

# Draw grids on the canvases
draw_grid(player_canvas, 10, 10, 20)
draw_grid(ai_canvas, 10, 10, 20)

# Create a label within the status frame for displaying game status
status_label = tk.Label(status_frame, text="Preparing Game", bg="lightgray", font=("Arial", 16))
status_label.pack(pady=20)

# Start the main loop
root.mainloop()
