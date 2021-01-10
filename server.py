import socket



sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("0.0.0.0", 7654))

sock.listen(12)

cli_sock, cli_add = sock.accept()
print("connection from" + str(cli_add[1]))
message = cli_sock.recv(12)
print(message.decode())