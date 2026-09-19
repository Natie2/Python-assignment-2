import socket

HOST = "127.0.0.1"
PORT = 5000

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()

    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)

        if data:
            print("Message from client:", data.decode())

except socket.error as e:
    print("Network error:", e)

finally:
    try:
        server_socket.close()
    except NameError:
        pass