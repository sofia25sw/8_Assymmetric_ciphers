import socket
import pickle
from random import randint

def cript(a1, key):
    a2 = [chr(ord(a1[i]) ^ key) for i in range(len(a1))]
    return ''.join(a2)

def sen(sock, msg, K):
    msg = cript(msg, K)
    sock.send(pickle.dumps(msg))

def rec(sock, K):
    msg = pickle.loads(sock.recv(1024))
    msg = cript(msg,K)
    return msg

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = [randint(0,250) for i in range(3)]
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))
B = pickle.loads(sock.recv(1024))
K = B ** a % p

print('Введите сообщение')
msg = input()

while msg != 'exit':
    sen(sock,msg, K)
    print(rec(sock,K))
    msg = input()

sock.close()