import socket
from pyDes import *

def get_predefined_key():
   
    return b"\x31\x41\x61\x11\x21\x31\x41\x51"

def decrypt_message(ciphertext, key):
   # Krijo një objekt DES me çelësin dhe modalitetin ECB
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
   # Dekripto ciphertext-in duke përdorur DES
    decrypted_message = desi.decrypt(ciphertext)
    return decrypted_message
# Funksioni për të enkriptuar një mesazh
def encrypt_message(message, key):
    desi = des(key, ECB, pad=None, padmode=PAD_PKCS5)
    encrypted_message = desi.encrypt(message)
    return encrypted_message
def server_program():
    host = '127.0.0.1'  # IP adresa lokale
    port = 5001  # Porti që serveri është i lidhur me te

    key = get_predefined_key()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("----------------------------------------------")
    print('Serveri është i gatshëm të pranojë lidhje...')
    print("-----------------------------------------------")
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
        
        prompt = "Serveri ka pranuar mesazhin, a deshironi te shihni permbajtjen?(p/j):"
        encrypted_prompt = encrypt_message(prompt, key)
        conn.send(encrypted_prompt)

        answer = conn.recv(16)
        decrypted_answer = decrypt_message(answer, key)
        decrypted_answer = decrypted_answer.decode()
        if decrypted_answer == 'p':
            conn.send(data)
        elif decrypted_answer == 'j':
            conn.send(b"")
        
        conn.close()

if __name__ == '__main__':
    server_program()
