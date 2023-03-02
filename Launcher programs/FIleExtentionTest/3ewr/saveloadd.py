import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import zlib

KEY = b'97F6A9765747DA88'

def save_file():
    data = input_text.get().encode()
    compressed_data = zlib.compress(data)
    cipher = AES.new(KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(compressed_data)
    file_name = filedialog.asksaveasfilename(defaultextension='.vr', filetypes=[("VR Files", "*.vr")])
    if file_name:
        with open(file_name, 'wb') as file:
            file.write(cipher.nonce)
            file.write(tag)
            file.write(ciphertext)
            output_text.delete('1.0', tk.END)
            output_text.insert(tk.END, f'Saved file: {file_name}')


def load_file():
    filename = filedialog.askopenfilename(defaultextension=".vr")
    with open(filename, "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
    compressed_data = cipher.decrypt_and_verify(ciphertext, tag)
    data = zlib.decompress(compressed_data)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, data.decode())

window = tk.Tk()

input_text = tk.Entry(window, width=100)
input_text.pack()

save_button = tk.Button(window, text='Save', command=save_file)
save_button.pack()

load_button = tk.Button(window, text='Load', command=load_file)
load_button.pack()

output_text = tk.Text(window)
output_text.pack()

window.mainloop()
