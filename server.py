import socket
from pyDes import *

def encrypt_message(message, key):
    desi = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    return desi.encrypt(message)

def decrypt_message(ciphertext, key):
    desi = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    return desi.decrypt(ciphertext)

def server_program():
    s = socket. socket()

    print('Socket succesfully created')

    port = 5001
    s. bind(('', port))
    print(f'socket binded to port{port}')
    s.listen(5)

    print( 'Socket is listening')
    key = "DESCrypt"  # 8-byte key for DES

    while True:
        c, addr = s.accept()
        print( 'Got connection from', addr)
        message = encrypt_message("Thank you for connecting",key)
        #print(message)
        c.send(message)
        c.close()
    '''host = socket.gethostname()
    port = 5001

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(5)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    key = "DESCrypt"  # 8-byte key for DES

    while True:
        data = conn.recv(1024)
        if not data:
            break
        decrypted_data = decrypt_message(data, key)
        print("Received from client: " + decrypted_data.decode())
        message = input(' -> ')
        encrypted_message = encrypt_message(message, key)
        conn.send(encrypted_message)
    conn.close()'''

if __name__ == '__main__':
    server_program()
