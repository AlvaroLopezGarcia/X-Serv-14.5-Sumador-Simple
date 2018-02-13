#!/usr/bin/python3

import socket
import random
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        request = str(recvSocket.recv(1024))
        resource = request.split()[1]
        _,num1,operador,num2 = resource.split('/')
        answer = num1+" "+operador+" "+num2+" = "+ str(calculadora.funciones[operador](int(num1),int(num2)))
        print(answer)
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n"+answer+"\r\n", 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
