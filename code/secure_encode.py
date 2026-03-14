from PIL import Image
import numpy as np
from Crypto.Cipher import AES
import hashlib
import base64

def get_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt_message(message, password):
    key = get_key(password)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    encrypted = base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')
    return encrypted

def message_to_binary(message):
    return ''.join(format(ord(i), '08b') for i in message)

def hide_data(image_name, secret_data, output_image_name):
    image = Image.open(image_name)
    np_image = np.array(image)
    total_bytes = np_image.size // 8

    if len(secret_data) > total_bytes:
        raise ValueError("[!] Data too large for this image")

    secret_data += '#####'
    binary_secret_data = message_to_binary(secret_data)
    data_index = 0

    for values in np_image:
        for pixel in values:
            for n in range(3):
                if data_index < len(binary_secret_data):
                    binary_pixel = format(pixel[n], '08b')
                    pixel[n] = int(binary_pixel[:-1] + binary_secret_data[data_index], 2)
                    data_index += 1
            if data_index >= len(binary_secret_data):
                break
        if data_index >= len(binary_secret_data):
            break

    encoded_image = Image.fromarray(np_image)
    encoded_image.save(output_image_name)
    print("[+] Data hidden successfully in", output_image_name)


if __name__ == "__main__":
    image_name = input("Enter input image file name: ")
    output_image = input("Enter output image file name: ")
    password = input("Enter password: ")

    message = input("Enter secret message: ")
    encrypted = encrypt_message(message, password)

    hide_data(image_name, encrypted, output_image)
