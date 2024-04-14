import socket

class ContentProvider2:
    def __init__(self):
        self.server_address = ('localhost', 8888)  # Server address

    def send_content(self, content):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.server_address)
            sock.sendall(content.encode())
            print("Content sent to the server by CP2")

if __name__ == "__main__":
    cp2 = ContentProvider2()
    cp2.send_content("Content from CP2")
