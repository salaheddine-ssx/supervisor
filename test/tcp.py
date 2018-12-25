from cryptography.fernet import Fernet
#key=Fernet.generate_key()
key="EbJZe1R8CDurOm-9BgPvW03MbgrzRicm17JtMSo2WOA="
import socket
TCP_IP = "127.0.0.1"
TCP_PORT = 9999
MESSAGE = """	<hello>
			<host_infos>
				<ip value="127.0.0.1" />
				<port value="9998" />
			</host_infos>
			<request>
				<get name="get_cpu_usage" />
				<get name="get_cpu_times" />
				<get name="get_cpu_count_logical" />
				<get name="get_cpu_count_physical" />
				<get name="get_cpu_stats" />
				<get name="get_cpu_freq" />
				<get name="get_vir_memory" />
				<get name="get_swap_memory" />
				<get name="get_disk_partitions" />
				<get name="get_disk_usage" />
				<get name="get_net_io_counters" />
				<get name="get_connections" />
				<get name="get_if_addr" />
				<get name="get_boot_time" />
				<get name="get_users" />
                                <get name="doesnt exist" />
			</request>
		</hello>
	"""

#from bs4 import BeautifulSoup as bs 
#sp=bs(MESSAGE,'lxml')
#print sp.request
#exit()
print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "message:", MESSAGE
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
MESSAGE+=" " * ((4 - len(MESSAGE) % 4) % 4)
sock.connect((TCP_IP,TCP_PORT))

sock.send(Fernet(key).encrypt(MESSAGE))

print "recieved data :"
sock.settimeout(30)
d=""
while True :
    try :
        a=sock.recv(1024)
        if a=="" :
            break
        d+=a
        print "**********"
        print d
        print "**********"
    except Exception as e:
        print "Exception:" , str(e)
        break

try :
    sock.close()
except :
    pass

print d
