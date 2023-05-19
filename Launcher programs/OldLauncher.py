import tkinter as tk
import os

# Define the functions to execute the batch scripts
def script1():
    os.system('start Installer.bat')

def script2():
    os.system('start Uninstaller.bat')

def script3():
    os.system('start LaunchDesktop.bat')

def script4():
    os.system('start LaunchVR.bat')

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
        os.system(f'start "{exe_path}"')
    else:
        tk.messagebox.showerror('Error', 'Could not find OpenNoteBlockStudio executable.')

# Create the GUI window
root = tk.Tk()
root.title('Batch Script Launcher')

# Create the buttons and add them to the window
button1 = tk.Button(root, text='Install', command=script1)
button1.pack()

button2 = tk.Button(root, text='Uninstall', command=script2)
button2.pack()

button3 = tk.Button(root, text='Launch', command=script3)
button3.pack()

button4 = tk.Button(root, text='Script 4', command=script4)
button4.pack()

button5 = tk.Button(root, text='OpenNoteBlockStudio', command=open_note_block_studio)
button5.pack()

# Start the GUI event loop
root.mainloop()
