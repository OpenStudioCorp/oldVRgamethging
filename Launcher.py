import tkinter as tk
import os
from tkinter import messagebox
#This is the new launcher. it is in poor condition but if you want to help make it. 
# just clone it and make a pull request
# Define the functions to execute the batch scripts
def script1():
    os.system('start 2.bat')

def script2():
    os.system('start 1.bat')

def script3():
    os.system('start Updater.bat')

def script4():
    os.system('start script4.bat')

def open_note_block_studio():
    exe_path = None
    # Search for the executable file in common installation locations
    search_paths = [
        r'C:\Program Files\OpenNoteBlockStudio\OpenNoteBlockStudio.exe',
        r'C:\Program Files (x86)\OpenNoteBlockStudio\OpenNoteBlockStudio.exe',
        r'C:\OpenNoteBlockStudio\OpenNoteBlockStudio.exe',
        r'%APPDATA%\ONBS\OpenNoteBlockStudio.exe'
    ]
    for path in search_paths:
        expanded_path = os.path.expandvars(path)
        if os.path.isfile(expanded_path):
            exe_path = expanded_path
            break
    if exe_path:
        os.system(f'start "" "{exe_path}"')
    else:
        messagebox.showerror('Error', 'Could not find OpenNoteBlockStudio executable.')

# Create the GUI window
root = tk.Tk()
root.title('OPENNBSVR LAUNCHER')

# Define the font for the button labels
button_font = ('Arial', 20)

# Create the buttons and add them to the window
button1 = tk.Button(root, text='Install', font=button_font, command=script1, width=20, height=2)
button1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

button2 = tk.Button(root, text='Uninstall', font=button_font, command=script2, width=20, height=2)
button2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

button3 = tk.Button(root, text='Update', font=button_font, command=script3, width=20, height=2)
button3.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

button4 = tk.Button(root, text='Unused for now', font=button_font, command=script4, width=20, height=2)
button4.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

button5 = tk.Button(root, text='OpenNoteBlockStudio', font=button_font, command=open_note_block_studio, width=20, height=2)
button5.grid(row=1, column=1, padx=10, pady=10, sticky='nsew', columnspan=2)

# Configure the row and column weights to make the buttons resize with the window
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Set the window size and center it on the screen
root.geometry('640x480')
root.eval('tk::PlaceWindow . center')

# Start the GUI main loop
root.mainloop()
