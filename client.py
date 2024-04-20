import socket
from pyDes import *

# Funksioni për të marrë çelësin e paracaktuar
def get_predefined_key():
    
    return b"\x31\x41\x61\x11\x21\x31\x41\x51"
# Funksioni për të enkriptuar një mesazh
def encrypt_message(message, key):
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    encrypted_message = desi.encrypt(message)
    return encrypted_message
# Klienti
def client_program():
    host = '127.0.0.1'  # IP adresa e serverit
    port = 5001  # Porti që serveri është i lidhur me

    key = get_predefined_key()
    print("--------------------------------------------------------")
    message = input("Shkruaj një mesazh për të dërguar në server: ")
    print("--------------------------------------------------------")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Lidhu me serverin
        s.connect((host, port))
     
        encrypted_message = encrypt_message(message, key)
        print("-----------------------------------------------------------------------------")
        print(f'Mesazhi është enkriptuar "{encrypted_message}" dhe është dërguar në server.')
           print("---------------------------------------------------------------------------")
        # Dërgo mesazhin e enkriptuar në server
        s.send(encrypted_message)

if __name__ == '__main__':
    client_program()
