from threading import Thread
from time import sleep
import socket

port = 10507

address = '0.0.0.0'

acessos = 0

def handle_http_request(request):
    pass

def handle_http_response():
    response = f'''
HTTP/1.0 200 OK
Date: Tue, 14 Mar 2023 15:11:00 GMT-3
Server: AulaRedes/1.0
Content-Type: text/HTML
 
<html>
    <head>
        <title>
            Aula de Redes
        </title>
    </head>

    <body>
        <h1>
            Aulda bacaninha de redes do dia 14
        </h1>

        <h2>
            IFPR Cascavel
        </h2>

        Este servidor foi acessado {acessos} vezes.<br>

        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdCHvGYDjWUQ1tx1825KNWvWkaWY4CGht0Pw&usqp=CAU"></img>

    </body>
</html>
'''

    return response

# class contador(Thread):
#     def __init__(self, n, segundos, nome):
#         Thread.__init__(self)
#         self.n = n
#         self.segundos = segundos
#         self.nome = nome

#     def run(self):
#         for i in range(self.n):
#             print(f'{self.nome}:{i+1}')
#             sleep(self.segundos)

class ThreadServer(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        data = self.conn.recv(4096)
        msg_recv = data.decode()

        handle_http_request(msg_recv)
        msg_snt = handle_http_response()

        self.conn.send(msg_snt.encode())



def main():
    global acessos

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((address, port))
    server.listen()

    while True:
        print('== Servidor aguardando conexões ==')
        acessos += 1
        conn, addr = server.accept()
        ThreadServer(conn, addr).start()

    # contador(5, 3, 'Guilhermina').start()
    # contador(10, 2, 'Magaiver').start()
    # contador(15, 1, 'Thanos').start()


if __name__ == '__main__':
    main()

