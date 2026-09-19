import socket

HOST = "127.0.0.1"
PORT = 5000

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    message = "Hello from client!"
    client_socket.sendall(message.encode("utf-8"))

    print("Message sent successfully.")

except socket.error as e:
    print("Network error:", e)

finally:
    try:
        client_socket.close()
    except NameError:
        pass
