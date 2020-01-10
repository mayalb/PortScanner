import socket
import os

s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ''
port = 80
s.bind((host,port))
s.listen(1)

print("Server port :",port,"Index: [/] = index.html","\n-----------------------------------------------")
hal = "index.html"
while True:
 con,address = s.accept()
 header = con.recv(2048).decode('utf-8')
 if len(header)>2:
  head = header.split(' ')
  request = head[1]
  method = head[0]
  if method=='GET':
   print("Request From : [{},{}] METHOD :[{}]  PATH :[{}] ".format(address[0],address[1],method,request))
  else:
   print("Request From : [{},{}] METHOD :[{}] PATH :[{}] ".format(address[0],address[1],method,request))
 else:
  request=hal 
 if request=='/':
  request =hal
 try:
  response = open(request.lstrip('/'),'rb')
  file = response.read()
  response.close()
  #header
  s_header = 'HTTP/1.1 OK 200\n'
  s_header += 'Content-Type: text/html\n\n'
 except:
  dt = open("not_found.html","r")
  file = dt.read().encode('utf-8')	
  s_header = 'HTTP/1.1 404 Not found\n'
  s_header += 'Content-Type: text/html\n\n'
 #final 
 final = s_header.encode('utf-8')
 final += file
  #send HEADER
 con.send(final)
 con.close()

