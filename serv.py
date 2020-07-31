import socket
import os
import sys

'''Самый простой эхо сервер для''' 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

while True:
    conn, adrr = s.accept()
    pid = os.fork()
    if child_pid == 0:
        data = conn.recv(1024)
        if (not data) or (data == 'close'):
            break
        conn.send(data)
        conn.close()
        sys.exit()
    else:
        conn.close()
