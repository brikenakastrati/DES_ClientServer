import socket
from pyDes import *


def get_predefined_key():
    
    return b"\x31\x41\x61\x11\x21\x31\x41\x51"

def encrypt_message(message, key):
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    encrypted_message = desi.encrypt(message)
    return encrypted_message
def decrypt_message(ciphertext, key):
   # Krijo një objekt DES me çelësin dhe modalitetin ECB
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
   # Dekripto ciphertext-in duke përdorur DES
    decrypted_message = desi.decrypt(ciphertext)
    return decrypted_message
# Klienti
def client_program():
    host = '127.0.0.1'  # IP adresa e serverit
    port = 5001  

    key = get_predefined_key()
    print("--------------------------------------------------------")
    message = input("Shkruaj një mesazh për të dërguar në server: ")
    print("--------------------------------------------------------")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Lidhu me serverin
        s.connect((host, port))
     
        encrypted_message = encrypt_message(message, key)
      
        print(f'Mesazhi është enkriptuar "{encrypted_message}" dhe është dërguar në server.')
        print("---------------------------------------------------------------------------")
        # Dërgo mesazhin e enkriptuar në server
          
        # Dergo mesazhin e enkriptuar ne server
        s.send(encrypted_message)
        prompt = s.recv(1024)
        decrypted_prompt = decrypt_message(prompt, key)
        print(decrypted_prompt.decode())

        answer = input("")
        encrypted_answer = encrypt_message(answer,key)
        s.send(encrypted_answer)

        decrypted_data = decrypt_message(s.recv(1024),key)
        print(decrypted_data.decode())
if __name__ == '__main__':
    client_program()
