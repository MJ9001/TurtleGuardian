# import the necessary packages
import time

# allow the cui8iamera to warmup
class Network:
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
    data = None
    def runNetwork(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while True:
                if len(data) > 0:
                    s.sendall(data.pop(0))
    
    def insert(self, line):
        data.push(line)    
    def __init__(self):
        x = threading.Thread(target=self.runCamera)
        x.start()
        print("Camera module initalized")

