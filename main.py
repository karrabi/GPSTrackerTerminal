import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9000


def main():
    port = 9000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((TCP_IP, TCP_PORT))
        while True:
            msg = input('Enter Message: ')
            s.sendall(msg.encode())
            resp = s.recv(1024)
            print('Received: ', resp.decode())

    s.close()


if __name__ == '__main__':
    main()
