import socket, threading

def scan_port(ip,port,lock):
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.settimeout(3)
 try:	
  try:
   dest = socket.getservbyport(port)
  except:
   dest = 'unknown'
  
  s.connect((ip,port))
  print(" [TCP]\tOPEN\t{}   {}".format(port,dest) )
 except:
  pass


ip = input("HOST :")
print("\nPROTO | STAT | PORT | SERV\n")


i = 0

lock = threading.Lock()

while(i<=65000):
 t = threading.Thread(target=scan_port, args=(ip,i,lock,) )
 lock.acquire()
 t.start()
 i+=1
 lock.release()

print("\nPort Scanned ({})".format(i))

