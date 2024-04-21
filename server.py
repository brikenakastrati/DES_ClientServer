import socket
from pyDes import *

def get_predefined_key():
   
    return b"\x31\x41\x61\x11\x21\x31\x41\x51"

def decrypt_message(ciphertext, key):
  
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
   # Dekripto ciphertext-in duke perdorur DES
    decrypted_message = desi.decrypt(ciphertext)
    return decrypted_message

def server_program():
    host = '127.0.0.1'  # IP adresa lokale
    port = 5001  

    key = get_predefined_key()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
   
    print('Serveri është i gatshëm të pranojë lidhje...')
    

  
    while True:
        conn, addr = s.accept()
        print("--------------------------------------------------------")
        print(f'U lidh klienti nga {addr}')
        print("--------------------------------------------------------")

        data = conn.recv(1024)
        decrypted_data = decrypt_message(data, key)
        print("--------------------------------------------------------")
        print(f'Mesazhi i dekriptuar nga klienti: {decrypted_data.decode()}')
        print("--------------------------------------------------------")
        
        conn.close()

if __name__ == '__main__':
    server_program()
