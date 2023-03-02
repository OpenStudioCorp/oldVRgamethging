import struct
import hashlib

def pad(data):
    padding = 16 - len(data) % 16
    return data + bytes([padding] * padding)

def unpad(data):
    padding = data[-1]
    if data[-padding:] != bytes([padding] * padding):
        raise ValueError("Invalid padding")
    return data[:-padding]

def encrypt(data, key):
    data = pad(data)
    key = hashlib.sha256(key.encode()).hexdigest()[:32]
    return ''.join(hex(ord(a) ^ ord(b))[2:] for a, b in zip(data, key))

def decrypt(data, key):
    key = hashlib.sha256(key.encode()).hexdigest()[:32]
    decrypted_data = bytes(int(data[i:i+2], 16) ^ ord(key[i//2]) for i in range(0, len(data), 2))
    return unpad(decrypted_data).decode()

def save_data(filename, data, key):
    encrypted_data = encrypt(data.encode(), key)
    with open(filename, 'wb') as file:
        file.write(struct.pack('<I', len(encrypted_data)))
        file.write(encrypted_data.encode())

def load_data(filename, key):
    with open(filename, 'rb') as file:
        encrypted_data_length = struct.unpack('<I', file.read(4))[0]
        encrypted_data = file.read(encrypted_data_length)
    decrypted_data = decrypt(encrypted_data.decode(), key)
    return decrypted_data
