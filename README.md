# SecureImageSteganography
Secure data transfer over internet using image steganography

This project implements secure data transfer using image steganography and encryption.

## Features
- AES encryption for message security
- LSB image steganography for hiding data
- Password-based decryption
- Secure message extraction

## Technologies Used
- Python
- NumPy
- Pillow
- PyCryptodome

## Files
secure_encode.py – Encrypts and hides message inside image  
secure_decode.py – Extracts and decrypts hidden message  

## How to Run

Install dependencies

pip install -r requirements.txt

### Encode Message

python secure_encode.py

### Decode Message

python secure_decode.py

## Applications
- Secure communication
- Digital watermarking
- Data hiding
