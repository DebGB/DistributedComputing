import socket

class Server:
    def __init__(self):
        self.address = ('localhost', 8888)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.address)
        self.socket.listen(1)
        print("Server listening...")

    def start(self):
        conn, addr = self.socket.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Server received:", data.decode())

if __name__ == "__main__":
    server = Server()
    server.start()
