import argparse
from os import path, listdir
import socket

parser = argparse.ArgumentParser()
parser.add_argument('--server', action='store_true', help='para indicar aplicação como servidora')
parser.add_argument('--host', default='localhost')
parser.add_argument('--port', default=50000)
parser.add_argument('--dir', default='.', help='diretório com arquivos para servir (ignorada se cliente)')
parser.add_argument('--file', default='/', help='arquivo para puxar (ignorada se servidor)')

args = parser.parse_args()

HOST = args.host
PORT = args.port

if not path.isdir(args.dir):
    print('argumento não é um diretório')
    exit(1)

FLIST = listdir(args.dir)


if args.server:
    print('\n'.join(FLIST))
    with socket.socket() as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(152)
                if not data: break
                req = str(data, 'utf-8').split(' ')
                if req[0] == 'GET':
                    if req[1] == '/':
                        ret = ('200 OK\n\n' + '\n'.join (FLIST))
                        conn.sendal(bytearray(ret, 'utf-8'))
                    else:
                        tmp = path.join(args.dir, req[1])
                        with open(tmp, 'rb') as f:
                            res = bytearray('200 OK\nLenght: {}\\n'.format(path.getsize(tmp)), 'utf-8')
                            data = f.read()
                            conn.sendall(b''.join([res, data]))

else: 
    with socket.socket() as s:
        s.connect((HOST, PORT))
        s.sendall(bytearray('GET {}'.format(args.file), 'utf-8'))
        data = s.recv(65535)
        print(str(data, 'utf-8'))
        s.close()



