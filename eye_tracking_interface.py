import socket
import time
from threading import Thread


class EyeTrackingInterface:
    host = "127.0.0.1"
    port = 43334
    running = False

    conn = None

    gaze_x = 0
    gaze_y = 0

    def __init__(self):
        self.receive_thread = None
        pass

    def stop(self):
        self.running = False

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print("Waiting for Tobii Eye Tracking to connect ...")
            self.conn, addr = s.accept()

            print("Tobii connected!")
            print("Starting listening Thread")

            self.running = True
            self.receive_thread = Thread(target=self.receive_data())
            self.receive_thread.start()

    def receive_data(self):
        print("sdfs")
        while self.running:
            print("test")
            time.sleep(0.05)
            data = self.conn.recv(1024)
            if not data:
                break
            print(data)
