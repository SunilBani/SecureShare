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

# Example usage
decrypt_file("encrypted_files/test.enc", "decrypted_files/test.txt", "keys/private.pem")
