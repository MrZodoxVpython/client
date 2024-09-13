import socket

def client():
    # Membuat socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Terhubung ke server di localhost dan port 12345
    client_socket.connect(('localhost', 12345))

    # Percakapan
    while True:
        # Input dari pengguna
        message = input("Anda: ")
        client_socket.send(message.encode('utf-8'))

        if message.lower() == 'keluar':
            break

        # Menerima respons dari bot
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

    client_socket.close()
    print("Koneksi ditutup.")

# Memulai client
client()
