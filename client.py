import socket
from pyDes import *
import os

def encrypt_message(message, key):
    desi = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    encrypted_message = desi.encrypt(message)
    return encrypted_message, key

def client_program():
    host = '127.0.0.1'  # IP adresa e serverit
    port = 5001  # Porti që serveri është i lidhur me

    key = os.urandom(8)  # Çelësi për DES gjeneruar në mënyrë të rastësishme
    message = input("Shkruaj një mesazh për të dërguar në server: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        encrypted_message, _ = encrypt_message(message, key)
        print(f'Mesazhi "{message}" është enkriptuar me çelësin e gjeneruar në mënyrë të rastësishme: {key} dhe është dërguar në server.')
        print(f'Mesazhi i enkriptuar: {encrypted_message}')

        # Dërgo çelësin në server
        s.send(key)
        # Dërgo mesazhin e enkriptuar në server
        s.send(encrypted_message)

if __name__ == '__main__':
    client_program()
