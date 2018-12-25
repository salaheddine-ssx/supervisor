import re
import time
import socket
from bs4 import BeautifulSoup as bs
import xml.dom.minidom
import threading
from cryptography.fernet import Fernet
import API.ressourceAPI as api
import ServerConf


class server :
	def __init__(self,port=9999,proto="tcp",host="localhost"):
		self.port=port
		self.proto=proto
		self.host=host

	def responder(self,srv_sock,addr):
		print "begin responder : %s:%s"%(addr[0],addr[1])
		print "recieved data"
                srv_sock.settimeout(5)
                data=""

                while True :
                    try :
                        data+=srv_sock.recv(1024)
                    except :
                        break

		print data
		print "decrypting data"
		data_=Fernet(ServerConf.key).decrypt(data)
		#s = re.sub('\s\s+','',data_)
		print xml.dom.minidom.parseString(data_).toprettyxml()
		print "extracing requested modules"
		soup=bs(data_,'lxml')
		print "server info:"
		ip=soup.host_infos.ip['value']
		print "+ip:",ip
		port=soup.host_infos.port['value']
		print "+port:",port
		print "modules:"
		res="<hello_back>"
		for elm in soup.request.find_all("get"):
			print "|_______",elm['name']
			res+="<frame>"+api.xmlise_data(elm['name'])+"</frame>"

		res+="</hello_back>"

		print "response to be sent"
		#res_=re.sub('\s\s+','',res)
		print xml.dom.minidom.parseString(res).toprettyxml()
		srv_sock.send(xml.dom.minidom.parseString(res).toprettyxml())
                time.sleep(3)
                srv_sock.close()
                print "socket closed"
		print "end responder : %s:%s"%(addr[0],addr[1])

	def run(self):
                try :
		    print "RUN %s:%s CTRL-C to exit"%(self.host,self.port)
		    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
		    sock.bind((self.host, self.port))
                    sock.listen(5)
		    while True :
			    #data, addr = sock.recvfrom(1024)
                            srv_sock,addr = sock.accept()
			    threading.Thread(target=self.responder,args=(srv_sock,addr)).start()
                except KeyboardInterrupt as e :
                    sock.close()
                    print "run function exited : ",str(e)
if __name__=="__main__":
	server().run()
