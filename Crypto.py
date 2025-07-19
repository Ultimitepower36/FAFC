from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os
import base64
import json
"""
password = b"mysecretpassword"  # Password must be in bytes

salt = os.urandom(16)  # Generate a random salt for security
"""

_mysalt = b'\xf1o\x0ef2l\xae\xe8)\xfbD|q\xd0\xbc\xe6'  # Generate a random salt for security

def derive_key(password):
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # Desired key length in bytes (e.g., 32 for AES-256)
            salt=_mysalt,
            iterations=100000,  # High iteration count for security
            backend=default_backend()
    )

    key_bytes = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key_bytes).decode()
 
def encrypt(data, password, save_file):
    cipher = Fernet(derive_key(password))
    data = json.dumps(data).encode()

    encrypted_file = cipher.encrypt(data)

    with open(save_file, "wb") as ef:
        ef.write(encrypted_file)


def decrypt(password, file) -> list:
    cipher = Fernet(derive_key(password))

    with open(file, "rb") as f:
        cipher_bytes = f.read()

    clear_text = cipher.decrypt(cipher_bytes)
    return json.loads(clear_text)


if __name__=="__main__":
    password = b"mysecretpassword"  # Password must be in bytes






    