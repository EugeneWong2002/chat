import socket


sock = socket.socket()
sock.connect(("127.0.0.1", 7654))
sock.send("Hello world!".encode())