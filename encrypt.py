from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('script.py', 'rb') as file:
    original_content = file.read()

cipher_suite = Fernet(key)
encrypted_content = cipher_suite.encrypt(original_content)

with open('encrypted.py', 'wb') as file:
    file.write(b"from cryptography.fernet import Fernet\n\n")
    file.write(b"key = " + repr(key).encode() + b"\n\n")  
    file.write(b"cipher_suite = Fernet(key)\n")
    file.write(b"encrypted_content = " + repr(encrypted_content).encode() + b"\n\n") 
    file.write(b"decrypted_content = cipher_suite.decrypt(encrypted_content)\n")
    file.write(b"exec(decrypted_content)\n")

print("Encryption completed successfully.")
