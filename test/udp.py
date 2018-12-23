from cryptography.fernet import Fernet
#key=Fernet.generate_key()
key="EbJZe1R8CDurOm-9BgPvW03MbgrzRicm17JtMSo2WOA="
import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 9999
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
			</request>
		</hello>
	"""
#from bs4 import BeautifulSoup as bs 
#sp=bs(MESSAGE,'lxml')
#print sp.request
#exit()
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
MESSAGE+=" " * ((4 - len(MESSAGE) % 4) % 4)
print len(MESSAGE)
sock.sendto(Fernet(key).encrypt(MESSAGE) , (UDP_IP, UDP_PORT))
