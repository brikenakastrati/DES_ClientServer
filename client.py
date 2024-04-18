import socket
from pyDes import *

def encrypt_message(message, key):
    desi = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    return desi.encrypt(message)

def decrypt_message(ciphertext, key):
    desi = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    return desi.decrypt(ciphertext)

def server_program():
    s = socket.socket()
    port = 5001
    s.connect(('127.0.0.1', port))
    message = s.recv(1024)
    key = "DESCrypt"  # 8-byte key for DES
    decrypted_message = decrypt_message(message, key)
    print(decrypted_message.decode())
    s.close()
    '''host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(5)
    
    key = "DESCrypt"  # 8-byte key for DES

    try:
        while True:
            conn, address = server_socket.accept()
            print("Connection from: " + str(address))

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decrypted_data = decrypt_message(data, key)
                print("Received from client: " + decrypted_data.decode())
                message = input(' -> ')
                encrypted_message = encrypt_message(message, key)
                conn.send(encrypted_message)
            conn.close()
    except KeyboardInterrupt:
        print("\nExiting server program...")
        server_socket.close()'''

if __name__ == '__main__':
    server_program()
