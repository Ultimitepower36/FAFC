from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os
import base64
"""
password = b"mysecretpassword"  # Password must be in bytes

salt = os.urandom(16)  # Generate a random salt for security
"""




password = b"mysecretpassword"  # Password must be in bytes

mysalt = b'\xf1o\x0ef2l\xae\xe8)\xfbD|q\xd0\xbc\xe6'  # Generate a random salt for security

kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Desired key length in bytes (e.g., 32 for AES-256)
        salt=mysalt,
        iterations=100000,  # High iteration count for security
        backend=default_backend()
)

key = base64.urlsafe_b64decode(kdf.derive(password))
cipher = Fernet(key)

with open("SaveData\Test.txt", "rb") as f:
    e_file = f.read()

encrypted_file = cipher.encrypt(e_file)

with open("SaveData\Test.txt", "wb") as ef:
    ef.write(encrypted_file)
