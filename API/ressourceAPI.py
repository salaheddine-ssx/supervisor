import psutil
import datetime
import xml.dom.minidom

def get_cpu_usage():
    return tuple(psutil.cpu_percent(interval=1,percpu=True))
    #[0.0, 0.0, 0.0, 3.0]

def get_cpu_times():
    d=[]
    for elm in psutil.cpu_times_percent(interval=1, percpu=True):
	r={}
	for e in ["user","nice","system","idle","iowait","irq","softirq","steal","guest","guest_nice"] :
		if e not in elm._fields:
			r[e]="?"
			continue
		r[e]=elm._asdict()[e]
        #r["user"]=elm.user
        #r["nice"]=elm.nice
        #r["system"]=elm.system
        #r["idle"]=elm.idle
        #r["iowait"]=elm.iowait
        #r["irq"]=elm.irq
        #r["softirq"]=elm.softirq
        #r["steal"]=elm.steal
        #r["guest"]=elm.guest
        #r["guest_nice"]=elm.guest_nice
	d.append(r)
    return d

    #[  
    #    {'softirq': 0.0, 'idle': 98.0, 'user': 2.0, 'guest_nice': 0.0, 'irq': 0.0, 'iowait': 0.0, 'steal': 0.0, 'system': 0.0, 'guest': 0.0, 'nice': 0.0},
    #    {'softirq': 0.0, 'idle': 99.0, 'user': 1.0, 'guest_nice': 0.0, 'irq': 0.0, 'iowait': 0.0, 'steal': 0.0, 'system': 0.0, 'guest': 0.0, 'nice': 0.0},
    #    {'softirq': 0.0, 'idle': 100.0, 'user': 0.0, 'guest_nice': 0.0, 'irq': 0.0, 'iowait': 0.0, 'steal': 0.0, 'system': 0.0, 'guest': 0.0, 'nice': 0.0},
    #    {'softirq': 0.0, 'idle': 99.0, 'user': 1.0, 'guest_nice': 0.0, 'irq': 0.0, 'iowait': 0.0, 'steal': 0.0, 'system': 0.0, 'guest': 0.0, 'nice': 0.0}
    #]
    #

def get_cpu_count_logical():
    return (psutil.cpu_count(logical=True),)

def get_cpu_count_physical():
    return (psutil.cpu_count(logical=False),)

def get_cpu_stats():
    a=psutil.cpu_stats()
    return {    "ctx_switches":a.ctx_switches,
                "interrupts":a.interrupts,
                "soft_interrupts":a.soft_interrupts,
                "syscalls":a.syscalls
        }
    #   {
    #    'interrupts': 60691200,
    #    'soft_interrupts': 61149301,
    #    'syscalls': 0,
    #    'ctx_switches': 189266891
    #    } 
    
def get_cpu_freq():
    a=psutil.cpu_freq(percpu=True)
    d=[]
    for elm in a :
        d.append({  "current":elm.current,
                    "min":elm.min,
                    "max":elm.max
                })
    return d

    #[
    #    {'current': 2083.561, 'max': 2700.0, 'min': 500.0},
    #    {'current': 1233.341, 'max': 2700.0, 'min': 500.0},
    #    {'current': 1197.383, 'max': 2700.0, 'min': 500.0},
    #    {'current': 1197.283, 'max': 2700.0, 'min': 500.0}
    #]

def get_vir_memory():
    a=psutil.virtual_memory()
    return {
                "total":a.total  if ("total" in a._fields) else "?" ,
                "available":a.available if ("available" in a._fields) else "?" ,
                "percent":a.percent if ("percent" in a._fields) else "?",
                "used":a.used if ("used" in a._fields) else "?",
                "free":a.free if ("free" in a._fields) else "?",
                "active":a.active if ("active" in a._fields) else "?",
                "inactive":a.inactive if ("inactive" in a._fields) else "?",
                "buffers":a.buffers if ("buffers" in a._fields) else "?",
                "cached":a.cached if ("cached" in a._fields) else "?",
                "shared":a.shared if ("shared" in a._fields) else "?"
            }
    #{
    #        'available': 1012891648,
    #        'cached': 894103552,
    #        'used': 2515259392,
    #        'buffers': 73453568,
    #        'inactive': 1062477824,
    #        'active': 2117816320,
    #        'shared': 263602176,
    #        'total': 4040368128,
    #        'percent': 74.9,
    #        'free': 557551616
    #}

def get_swap_memory():
    #sswap(total=4192202752, used=1069948928, free=3122253824, percent=25.5, sin=866160640, sout=1928462336)
    a=psutil.swap_memory()
    return {
            "total":a.total,
            "used":a.used,
            "free":a.free,
            "percent":a.percent,
            "sin":a.sin,
            "sout":a.sout
            }
    #{
    #'used': 1069948928,
    #'percent': 25.5, 
    #'free': 3122253824, 
    #'sout': 1928462336, 
    #'total': 4192202752, 
    #'sin': 866160640
    #}

def get_disk_partitions():
    #sdiskpart(device='sysfs', mountpoint='/sys', fstype='sysfs', opts='rw,nosuid,nodev,noexec,relatime')
    return [ {'device':elm.device,'mountpoint':elm.mountpoint ,'fstype':elm.fstype,'opts':elm.opts} for elm in psutil.disk_partitions(all=True)]
def get_disk_usage():
    a=get_disk_partitions()
    d=[]
    #sdiskusage(total=0, used=0, free=0, percent=0.0)
    for elm in a :
        d.append({  'device':elm['device'],
                    'mountpoint':elm['mountpoint'],
                    'fstype':elm['fstype'],
                    'opts':elm['opts'],
                    'total':psutil.disk_usage(elm['mountpoint']).total ,
                    'used':psutil.disk_usage(elm['mountpoint']).used ,
                    'free':psutil.disk_usage(elm['mountpoint']).free ,
                    'percent':psutil.disk_usage(elm['mountpoint']).percent
                }
                )
    return d 

def xmlise_data(function_name):
    print "xmlise_date called with argument : %s "%type(function_name) ,function_name
    string="<%s>"%function_name
    try :
        data=globals()[function_name]()
        if type(data) is tuple :
            for i,elm in enumerate(data) :
                string+="<data id='%d' value='%s' />"%(i,str(elm))
        elif type(data) is list :
            for i,elm in enumerate(data):
                string+="<data id='%d' >"%i
                for k in elm.keys():
                    string+="<item name='%s' value='%s' />"%(k,str(elm[k]))
                string+="</data>"
        elif type(data) is dict :
            for k in data.keys():
                string+="<data name='%s' value='%s' />"%(k,str(data[k]))

    except Exception as e :
        a=repr(e)+" in xmlise_data"
        string+="""<exception value="%s" />"""%str(a)


    string+="</%s>"%function_name

    return xml.dom.minidom.parseString(string).toprettyxml()


def get_net_io_counters():
	data=psutil.net_io_counters(pernic=True, nowrap=True)
	r=[]
	for k,v in data.items():
		r.append({	"interface":k,
				"bytes_sent":v.bytes_sent,
				"bytes_recv":v.bytes_recv,
				"packets_sent":v.packets_sent,
				"packets_recv":v.packets_recv,
				"errin":v.errin,
				"errout":v.errout,
				"dropin":v.dropin,
				"dropout":v.dropout
			})
	return r

def get_connections():
	data=psutil.net_connections(kind='inet')
	r=[]
	for elm in data :
		r.append({
				"fd":elm.fd,
				"family":elm.family,
				"type":elm.type,
				"laddr":elm.laddr.ip if type(elm.laddr)!=tuple else "*",
				"lport":elm.laddr.port if type(elm.laddr)!=tuple else "*",
				"raddr":elm.raddr.ip if type(elm.raddr)!=tuple else "*",
				"rport":elm.raddr.port if type(elm.raddr)!=tuple else "*",
				"status":elm.status,
				"pid":elm.pid
			})
	return r 
		
def get_if_addr():
	data=psutil.net_if_addrs()
	r=[]
	for k,v in data.items():
		for elm in v :
			r.append({
					"interface":k,
					"family":elm.family,
					"address":elm.address,
					"netmask":elm.netmask,
					"broadcast":elm.broadcast,
					"ptp":elm.ptp
				})
	return r 
def get_boot_time():
	return (datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S") ,)

def get_users():
	data=psutil.users()
	r=[]
	for elm in data :
		r.append({
				"name":elm.name,
				"terminal":elm.terminal,
				"host":elm.host,
				"started":elm.started,
				"pid":elm.pid
				})
		
	return r 
	
			
if __name__=="__main__":
	print get_vir_memory()
	print  xmlise_data('get_vir_memory')
