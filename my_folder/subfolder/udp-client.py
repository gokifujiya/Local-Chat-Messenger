import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = 'my_folder/subfolder/udp_socket_file'
client_address = 'my_folder/subfolder/udp_client_socket_file'

# Make sure the client address doesn't already exist
try:
    os.unlink(client_address)
except FileNotFoundError:
    pass

sock.bind(client_address)

try:
    while True:
        msg = input("Enter your message (type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break

        sock.sendto(msg.encode(), server_address)
        print("Waiting for reply...")

        data, _ = sock.recvfrom(4096)
        print("Server replied: {}".format(data.decode()))

finally:
    print("Closing socket")
    sock.close()
    os.unlink(client_address)
