import socket


s = socket.socket()
print('Socket Created')

s.bind(('192.168.15.94', 9999))

s.listen(3)

while True:
    x = str(input("Write Something :       "))
    c, addr = s.accept()
    c.send(bytes(x, 'utf-8'))
    name = c.recv(1024).decode()
    print(addr, "has written something to you : ", name)
