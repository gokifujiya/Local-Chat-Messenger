# socketとosモジュールをインポートします
import socket
import os

# UNIXソケットをストリームモードで作成します
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# このサーバが接続を待つUNIXソケットのパスを設定します
server_address = '/tmp/socket_file'

# 以前の接続が残っていた場合に備えて、サーバアドレスをアンリンク（削除）します
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

# サーバアドレスにソケットをバインド（接続）します
sock.bind(server_address)

# ソケットが接続要求を待機するようにします
sock.listen(1)

# 無限ループでクライアントからの接続を待ち続けます
while True:
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)

        # クライアントからのデータを一度だけ受け取ります
        data = connection.recv(1024)
        if data:
            data_str = data.decode('utf-8')
            print('Received:', data_str)
            response = 'Processing ' + data_str
            connection.sendall(response.encode())
        else:
            print('No data received')

    finally:
        print("Closing current connection")
        connection.close()
