import tkinter as tk
import tkinter.filedialog as filedialog
import subprocess

class SaveLoadGUI:
    def __init__(self, master):
        self.master = master
        master.title("SaveLoadGUI")

        # Create the text box for entering data
        self.text_box = tk.Text(master, height=10, width=30)
        self.text_box.pack(padx=10, pady=10)

        # Create the "Save" button
        self.save_button = tk.Button(master, text="Save", command=self.save_data)
        self.save_button.pack(padx=10, pady=5)

        # Create the "Load" button
        self.load_button = tk.Button(master, text="Load", command=self.load_data)
        self.load_button.pack(padx=10, pady=5)

        # Create the "Browse" button for choosing file location
        self.browse_button = tk.Button(master, text="Browse", command=self.choose_file)
        self.browse_button.pack(padx=10, pady=5)

        # Create the output box for displaying loaded data
        self.output_box = tk.Text(master, height=10, width=30)
        self.output_box.pack(padx=10, pady=10)

        # Initialize the filename variable
        self.filename = ""

    def choose_file(self):
        # Open the file dialog and get the chosen filename
        self.filename = filedialog.asksaveasfilename(defaultextension=".VIRT", filetypes=[("Virtual Files", "*.VIRT"), ("All Files", "*.*")])
        
    def save_data(self):
        if self.filename:
            # Get the data from the text box
            data = self.text_box.get("1.0", tk.END)

            # Save the data using the C# script
            subprocess.run(["dotnet", "save_load_manager.dll", "save", self.filename, data])
        else:
            # Show an error message if no filename has been chosen
            tk.messagebox.showerror("Error", "No file selected.")

    def load_data(self):
        if self.filename:
            # Load the data using the C# script
            output = subprocess.check_output(["dotnet", "save_load_manager.dll", "load", self.filename])

            # Display the loaded data in the output box
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, output.decode("utf-8"))
        else:
            # Show an error message if no filename has been chosen
            tk.messagebox.showerror("Error", "No file selected.")

if __name__ == '__main__':
    root = tk.Tk()
    app = SaveLoadGUI(root)
    root.mainloop()
