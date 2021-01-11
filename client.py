import socket


ip = input("Enter server ip: ")
port = input("Enter server port: ")

sock = socket.socket()
sock.connect((ip, int(port)))
message = input("Enter message: ")
sock.send(message.encode())