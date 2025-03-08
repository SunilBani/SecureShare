from Crypto.PublicKey import RSA

# Generate RSA key pair
key = RSA.generate(2048)

# Save the private key
private_key = key.export_key()
with open("keys/private.pem", "wb") as f:
    f.write(private_key)

# Save the public key
public_key = key.publickey().export_key()
with open("keys/public.pem", "wb") as f:
    f.write(public_key)

print("RSA Key Pair Generated!")
