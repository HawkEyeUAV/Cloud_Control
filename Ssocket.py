#!/usr/bin/env python
#encoding:utf-8
import socket
import threading
import time
import re
import MySQLdb as mdb
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('10.141.63.118',9000))
s.listen(5)
#a=[]
#b=[]
#c=[]
#tem=[]
#hum=[]
#distance=[]
#f=open('./data.txt','w')
print 'Waiting for connection...'

def main():
    while True:
        sock,addr=s.accept()
        t=threading.Thread(target=tcplink,args=(sock,addr))
        t.start()

def tcplink(sock,addr):
    print 'Accept new connection from %s:%s...' %addr
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
#        if data:
#        f=open('./data.txt','w+')
#        f.write(data)
#        f.close()
#        print data
        a=data
        b=re.split('f',a)
        c=re.split('a',b[1])
        tem=c[0]
        hum=c[1]
        distance=c[2]
        print c
        con = mdb.connect('127.0.0.1','root','19950419li','tencentcloud')
        cur = con.cursor()
        cur.execute('INSERT INTO home(id,updatetime,tem,hum,distance) VALUES(null,null,%s,%s,%s)',c)
        con.commit()
        cur.close()
        con.close()
        print 'tem is',tem
        print 'hum is',hum
        print 'distance',distance 
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s' %data).encode('utf-8'))
    sock.close()
#    f.close()
    print 'Connection from %s:%s closed' %addr
main() 
