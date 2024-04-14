# Pseudocode for User Node

import socket
import threading

class UserNode:
    def __init__(self, node_id):
        self.node_id = node_id
        
    def read_content(self, content):
        print(f"User {self.node_id} reads content: {content}")

# Function to handle user node connection
def handle_user_node(conn, addr):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        content = data.split(":")[1]
        user_id = data.split(":")[0]
        user_node = UserNode(user_id)
        user_node.read_content(content)
    conn.close()

# Usage

if __name__ == "__main__":
    user1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    user1_socket.connect(('localhost', 8888))
    user2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    user2_socket.connect(('localhost', 8888))
    
    user1_thread = threading.Thread(target=handle_user_node, args=(user1_socket, ('localhost', 8888)))
    user2_thread = threading.Thread(target=handle_user_node, args=(user2_socket, ('localhost', 8888)))
    
    user1_thread.start()
    user2_thread.start()
    
    # Simulate sending request to server for content
    user1_socket.send("User1:REQUEST".encode())
    user2_socket.send("User2:REQUEST".encode())
    
    # Simulate receiving content from server
    user1_socket.send("Content from CP1".encode())
    user2_socket.send("Content from CP2".encode())
    
    user1_thread.join()
    user2_thread.join()

