import socket
from pyDes import *
import os

def decrypt_message(ciphertext, key):
    desi = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    decrypted_message = desi.decrypt(ciphertext)
    return decrypted_message

def server_program():
    host = '127.0.0.1'  # IP adresa lokale
    port = 5001  # Porti që serveri është i lidhur me te

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    print('Serveri është i gatshëm të pranojë lidhje...')

    while True:
        conn, addr = s.accept()
        print(f'U lidh klienti nga {addr}')

        # Prano çelësin e dërguar nga klienti
        key = conn.recv(8)
        data = conn.recv(1024)
        
        decrypted_data = decrypt_message(data, key)
        print(f'Mesazhi i dekriptuar nga klienti: {decrypted_data.decode()}')
        
        conn.close()

if __name__ == '__main__':
    server_program()
