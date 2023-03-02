import os
import tkinter as tk
from tkinter import filedialog
import pynbs

# Create a Tkinter root window for the file dialog
root = tk.Tk()
root.withdraw()

# Open the file dialog to select an NBS file
file_path = filedialog.askopenfilename(filetypes=[("NBS files", "*.nbs")])
if not file_path:
    print("No file selected.")
    exit()

# Load the NBS file using pynbs
nbs = pynbs.read(file_path)

# Print the title and tempo of the NBS file
print(f"Title: {nbs.header.name}")
print(f"Tempo: {nbs.tempo}")










