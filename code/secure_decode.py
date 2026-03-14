from PIL import Image
import numpy as np
from Crypto.Cipher import AES
import hashlib
import base64

def get_key(password):
    return hashlib.sha256(password.encode()).digest()

def decrypt_message(encrypted, password):
    key = get_key(password)
    data = base64.b64decode(encrypted)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    message = cipher.decrypt_and_verify(ciphertext, tag)
    return message.decode('utf-8')

def binary_to_text(binary_data):
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_data = ''.join(chr(int(byte, 2)) for byte in all_bytes)
    return decoded_data

def reveal_data(image_name):
    image = Image.open(image_name)
    np_image = np.array(image)

    binary_data = ""
    for values in np_image:
        for pixel in values:
            for n in range(3):
                binary_data += format(pixel[n], '08b')[-1]

    all_data = binary_to_text(binary_data)
    secret_data = all_data.split("#####")[0]
    return secret_data

if __name__ == "__main__":
    image_name = input("Enter encoded image name: ")
    password = input("Enter password: ")

    hidden_data = reveal_data(image_name)
    try:
        decrypted = decrypt_message(hidden_data, password)
        print("[+] Hidden Message:", decrypted)
    except Exception as e:
        print("[!] Incorrect password or corrupted data")
