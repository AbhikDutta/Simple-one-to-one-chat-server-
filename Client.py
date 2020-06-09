import socket

while True:

    c = socket.socket()

    c.connect(('192.168.15.94', 9999))

    print(c.recv(1024).decode())

    name = input("Enter your response :      ")

    c.send(bytes(name, 'utf-8'))
