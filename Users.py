import socket

class User:
    def __init__(self):
        self.server_address = ('localhost', 8888)  # Server address

    def request_content(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.server_address)
            sock.sendall(b"REQUEST")
            data = sock.recv(1024)
            print("User received content:", data.decode())

if __name__ == "__main__":
    user = User()
    user.request_content()
