# Pseudocode for Content Provider

import socket
import threading
import hashlib

class ContentProvider:
    def __init__(self, provider_id, content):
        self.provider_id = provider_id
        self.content = content
        self.server_address = ('localhost', 8888)  # Server address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mutex = threading.Lock()
        
    def send_content(self):
        try:
            self.socket.connect(self.server_address)
            self.socket.send(f"CONTENT {self.provider_id}:{self.content}".encode())
            print(f"Content provider {self.provider_id} sent content to the server")
        finally:
            self.socket.close()


# Pseudocode for User Node

class UserNode:
    def __init__(self, node_id):
        self.node_id = node_id
        
    def read_content(self, content):
        print(f"User {self.node_id} reads content: {content}")


# Pseudocode for Server

class Server:
    def __init__(self):
        self.address = ('localhost', 8888)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mutex = threading.Lock()
        self.content_store = {}  # Dictionary to store unique content hashes and their contents
        
    def start(self):
        self.socket.bind(self.address)
        self.socket.listen(5)  # Listen for connections
        print("Server listening...")
        
        while True:
            conn, addr = self.socket.accept()
            threading.Thread(target=self.handle_request, args=(conn, addr)).start()
    
    def handle_request(self, conn, addr):
        try:
            data = conn.recv(1024).decode()
            if data.startswith("CONTENT"):
                self.receive_content(data.split(":")[1])
            elif data.startswith("REQUEST"):
                self.request_content(conn)
        finally:
            conn.close()
            
    def receive_content(self, content_data):
        provider_id, content = content_data.split(":")
        content_hash = hashlib.md5(content.encode()).hexdigest()
        
        self.mutex.acquire()
        if content_hash not in self.content_store:
            self.content_store[content_hash] = content
            print(f"Server stored content from provider {provider_id}")
        else:
            print(f"Content from provider {provider_id} is duplicate and not stored")
        self.mutex.release()
        
    def request_content(self, conn):
        self.mutex.acquire()
        for content_hash, content in self.content_store.items():
            conn.send(content.encode())
            print(f"Server sent content to user node: {content}")
        self.mutex.release()


# Usage

if __name__ == "__main__":
    server = Server()
    threading.Thread(target=server.start).start()
    
    # Create content providers
    cp1 = ContentProvider("CP1", "Content from CP1")
    cp2 = ContentProvider("CP2", "Content from CP2")
    cp3 = ContentProvider("CP3", "Content from CP3")
    
    # Create user nodes
    user1 = UserNode("User1")
    user2 = UserNode("User2")
    
    # Simulate content providers sending content to the server
    cp1.send_content()
    cp2.send_content()
    cp3.send_content()
    
    # Simulate user nodes requesting content from the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8888))
    
    server_socket.send("REQUEST".encode())
    
    # Receive content from the server
    user1.read_content(server_socket.recv(1024).decode())
    user2.read_content(server_socket.recv(1024).decode())

