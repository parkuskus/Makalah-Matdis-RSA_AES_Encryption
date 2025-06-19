import base64
import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

KEY_DIR = "data"
PUBLIC_KEY_PATH = os.path.join(KEY_DIR, "public.pem")
PRIVATE_KEY_PATH = os.path.join(KEY_DIR, "private.pem")

# Create key pair if not exists
if not os.path.exists(PUBLIC_KEY_PATH) or not os.path.exists(PRIVATE_KEY_PATH):
    os.makedirs(KEY_DIR, exist_ok=True)
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open(PRIVATE_KEY_PATH, "wb") as f:
        f.write(private_key)
    with open(PUBLIC_KEY_PATH, "wb") as f:
        f.write(public_key)

public_key = RSA.import_key(open("data/public.pem").read())
private_key = RSA.import_key(open("data/private.pem").read())

cipher_rsa_enc = PKCS1_OAEP.new(public_key)
cipher_rsa_dec = PKCS1_OAEP.new(private_key)

# Procedure for encrypting sensitive field (ex: password) using RSA + AES
def encrypt_sensitive_fields(password):
    aes_key = get_random_bytes(16)
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)

    data = password.encode()
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    encrypted_data = cipher_aes.nonce + tag + ciphertext
    encrypted_key = cipher_rsa_enc.encrypt(aes_key)

    return base64.b64encode(encrypted_data).decode(), base64.b64encode(encrypted_key).decode()

# Procedure for decrypting sensitive field (ex: password)
def decrypt_sensitive_fields(encrypted_data_b64, encrypted_key_b64):
    encrypted_data = base64.b64decode(encrypted_data_b64)
    encrypted_key = base64.b64decode(encrypted_key_b64)

    aes_key = cipher_rsa_dec.decrypt(encrypted_key)

    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]

    cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted.decode(),  # Return as single-element tuple for compatibility

# Procedure plain text --> cipher text using AES encryption
def aes_encrypt_only(plaintext: str) -> tuple[str, str]:
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())

    encrypted_data = cipher.nonce + tag + ciphertext
    return base64.b64encode(encrypted_data).decode(), base64.b64encode(key).decode()


# Procedure cipher text --> plain text using AES encryption
def aes_decrypt_only(cipher_b64, key_b64):
    from Crypto.Cipher import AES
    import base64

    encrypted_data = base64.b64decode(cipher_b64)
    aes_key = base64.b64decode(key_b64)

    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]

    cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted.decode()