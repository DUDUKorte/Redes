import socket

port = 10500
dest = 'localhost'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'== Conectando ao servidor {dest}:{port}')
client.connect((dest,port))

while True:
    msg = input('Mensagem: ')
    client.send(msg.encode())

    msg = client.recv(4096)
    print(f'Servidor: {msg.decode()}')

client.close()