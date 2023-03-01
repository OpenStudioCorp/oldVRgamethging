import struct
import hashlib
import base64
from Crypto.Cipher import AES

def pad(data):
    padding = AES.block_size - len(data) % AES.block_size
    return data + bytes([padding] * padding)

def unpad(data):
    padding = data[-1]
    if data[-padding:] != bytes([padding] * padding):
        raise ValueError("Invalid padding")
    return data[:-padding]

def encrypt(data, key):
    data = pad(data)
    iv = hashlib.sha256(key.encode()).digest()[:16]
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(data))

def decrypt(data, key):
    data = base64.b64decode(data)
    iv = data[:16]
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data[16:]))

def save_data(filename, data, key):
    encrypted_data = encrypt(data.encode(), key)
    with open(filename, 'wb') as file:
        file.write(struct.pack('<I', len(encrypted_data)))
        file.write(encrypted_data)

def load_data(filename, key):
    with open(filename, 'rb') as file:
        encrypted_data_length = struct.unpack('<I', file.read(4))[0]
        encrypted_data = file.read(encrypted_data_length)
    decrypted_data = decrypt(encrypted_data, key)
    return decrypted_data.decode()
