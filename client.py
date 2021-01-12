import socket


ip = input("Enter server ip: ")
port = input("Enter server port: ")

sock = socket.socket()
sock.connect((ip, int(port)))
while True:
    message = input("Enter message: ")
    if (message == "quit()"):
        sock.close()
        break
    sock.send(message.encode())