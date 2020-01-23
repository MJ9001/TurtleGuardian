# import the necessary packages
import time
import socket
import threading


class Network:
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 8878         # The port used by the server
    data = []
    def start(self):
        x = threading.Thread(target=self.runNetwork)
        x.start()
    def runNetwork(self):
        print(self.HOST)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            while True:
                if len(self.data) > 0:
                    s.sendall(str.encode(self.data.pop(0)))
        print("Network module initalized")
    
    def insert(self, line):
        self.data.append(line)   

    def test(self):
        self.insert("this is a test")

    def __init__(self):
        pass
