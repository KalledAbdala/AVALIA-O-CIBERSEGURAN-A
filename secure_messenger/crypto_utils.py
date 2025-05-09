from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# Chave secreta de 16 bytes (128 bits)
SECRET_KEY = b'MinhaChaveSecreta'

def encrypt_message(message):
    message_bytes = message.encode('utf-8')
    iv = get_random_bytes(16)
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(message_bytes, AES.block_size))
    return base64.b64encode(iv + encrypted).decode('utf-8')

def decrypt_message(encoded_message):
    raw = base64.b64decode(encoded_message)
    iv = raw[:16]
    encrypted = raw[16:]
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode('utf-8')
