import sys
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def decrypt_file(input_file, output_file, private_key_file):
    # Load private key
    with open(private_key_file, "rb") as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)

    with open(input_file, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    print(f"File '{input_file}' decrypted successfully!")

# Check for command-line arguments
if len(sys.argv) != 2:
    print("Usage: python receiver.py <encrypted_file>")
    sys.exit(1)

input_filename = sys.argv[1]
decrypt_file(f"encrypted_files/{input_filename}", f"decrypted_files/{input_filename.replace('.enc', '')}", "keys/private.pem")
