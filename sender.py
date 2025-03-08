import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_file(input_file, output_file, public_key_file):
    with open(public_key_file, "rb") as f:
        public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)

    with open(input_file, "rb") as f:
        file_data = f.read()

    encrypted_data = cipher.encrypt(file_data[:190])  # RSA 2048 limit

    with open(output_file, "wb") as f:
        f.write(encrypted_data)

    print(f"File '{input_file}' encrypted successfully!")

# Check if file argument is given
if len(sys.argv) != 2:
    print("Usage: python sender.py <file_name>")
    sys.exit(1)

input_filename = sys.argv[1]
encrypt_file(input_filename, f"encrypted_files/{input_filename}.enc", "keys/public.pem")
