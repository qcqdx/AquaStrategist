"""
AquaStrategist: Battleship Game

This file contains the main GUI for the AquaStrategist game. The GUI includes
two canvases representing the player's and AI's game boards.

Author: qcqdx
License: MIT License
"""

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("AquaStrategist - Battleship")
root.geometry("600x400")

# Create canvases for the game boards
# Player's game board (blue canvas on the left)
player_canvas = tk.Canvas(root, width=200, height=200, bg="blue")
# AI's game board (red canvas on the right)
ai_canvas = tk.Canvas(root, width=200, height=200, bg="red")

# Place the canvases in the window
player_canvas.pack(side="left", padx=20, pady=20)
ai_canvas.pack(side="right", padx=20, pady=20)

# Start the main loop
root.mainloop()
