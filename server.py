import socket


sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip = input("Enter ip: ")
port = input("Enter port: ")

sock.bind((ip, int(port)))

sock.listen(12)





cli_sock, cli_add = sock.accept()
print("Connection from " + str(cli_add[1]))
while True:
    try:
        message = cli_sock.recv(2048)
    except Exception as e:
        print("Something went wrong")
    else:
        print(message.decode())
