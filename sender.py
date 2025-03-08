from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import sys

def encrypt_file(input_file, output_file, public_key_file):
    # Load recipient's public key
    with open(public_key_file, "rb") as f:
        public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)

    with open(input_file, "rb") as f:
        file_data = f.read()

    encrypted_data = cipher.encrypt(file_data[:190])  # RSA 2048 limit

    with open(output_file, "wb") as f:
        f.write(encrypted_data)

    print(f"File '{input_file}' encrypted successfully!")

# Example usage
encrypt_file("test.txt", "encrypted_files/test.enc", "keys/public.pem")
