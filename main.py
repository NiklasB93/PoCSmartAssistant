import socket

HOST = "127.0.0.1"
PORT = 43334

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("waiting .. ")
    conn, addr = s.accept()
    print("accepted connection")
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
