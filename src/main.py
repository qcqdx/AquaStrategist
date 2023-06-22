"""
AquaStrategist: Battleship Game

This file contains the main GUI for the AquaStrategist game. The GUI includes
two sections representing the player's and AI's game boards, and a status section
for displaying the game state, such as score and messages.

Author: qcqdx
License: MIT License
"""

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("AquaStrategist - Battleship")
root.geometry("900x400")

# Create frames to section the window
# Frame for the player's game board (light blue background on the left)
player_frame = tk.Frame(root, width=300, height=300, bg="lightblue")
# Frame for the AI's game board (light coral background in the middle)
ai_frame = tk.Frame(root, width=300, height=300, bg="lightcoral")
# Frame for the game status (light gray background at the bottom)
status_frame = tk.Frame(root, width=600, height=100, bg="lightgray")

# Place the frames in the window
player_frame.pack(side="left", padx=20, pady=20)
ai_frame.pack(side="left", padx=20, pady=20)
status_frame.pack(side="bottom", padx=20, pady=20, fill="x")

# Create canvases within the respective frames for the game boards
# Player's game board canvas (blue)
player_canvas = tk.Canvas(player_frame, width=200, height=200, bg="blue")
# AI's game board canvas (red)
ai_canvas = tk.Canvas(ai_frame, width=200, height=200, bg="red")

# Place the canvases within the frames
player_canvas.pack(padx=20, pady=20)
ai_canvas.pack(padx=20, pady=20)

# Create a label within the status frame for displaying game status
status_label = tk.Label(status_frame, text="Preparing Game", bg="lightgray", font=("Arial", 16))
status_label.pack(pady=20)

# Start the main loop
root.mainloop()
