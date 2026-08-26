import base64

secret_message = "The vault combination is 42-17-89"

def encrypt(message, key):
    encoded_chars = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(message[i]) ^ ord(key_c))
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.b64encode(encoded_string.encode('utf-8')).decode('utf-8')

def decrypt(ciphertext, key):
    decoded_string = base64.b64decode(ciphertext.encode('utf-8')).decode('utf-8')
    decoded_chars = []
    for i in range(len(decoded_string)):
        key_c = key[i % len(key)]
        decoded_c = chr(ord(decoded_string[i]) ^ ord(key_c))
        decoded_chars.append(decoded_c)
    return "".join(decoded_chars)

# 1. Encrypt and write to file
encrypted_data = encrypt(secret_message, secret_key)
with open("secret_file.txt", "w") as f:
    f.write(encrypted_data)

print("Secret saved to 'secret_file.txt':", encrypted_data)

# 2. Read from file and decrypt
with open("secret_file.txt", "r") as f:
    stored_data = f.read()

revealed_message = decrypt(stored_data, secret_key)
print("Decrypted message:", revealed_message)
