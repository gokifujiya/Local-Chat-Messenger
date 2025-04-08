from faker import Faker
import socket
import os

faker = Faker()
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = 'my_folder/subfolder/udp_socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))
sock.bind(server_address)

while True:
    print('\nWaiting to receive message...')
    data, address = sock.recvfrom(4096)
    print('Received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        fake_reply = faker.sentence()  # Generate a fake response
        sent = sock.sendto(fake_reply.encode('utf-8'), address)
        print('Sent {} bytes back to {}'.format(sent, address))
