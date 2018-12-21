import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1,percpu=True)
    #[0.0, 0.0, 0.0, 3.0]


def get_cpu_times():
    d=[]
    for elm in psutil.cpu_times_percent(interval=1, percpu=True):
        d.append({  "user":elm.user,
                    "nice":elm.nice,
                    "system":elm.system,
                    "idle":elm.idle,
                    "iowait":elm.iowait,
                    "irq":elm.irq,
                    "softirq":elm.softirq,
                    "steal":elm.steal,
                    "guest":elm.guest,
                    "guest_nice":elm.guest_nice
                    })
    return d
    #[  
    #    {'softirq': 0.0, 'idle': 98.0, 'user': 2.0, 'guest_nice': 0.0, 'irq': 0.0, 'iowait': 0.0, 'steal': 0.0, 'system': 0.0, 'guest': 0.0, 'nice': 0.0},
    #    {'softirq': 0.0, 'idle': 99.0, 'user': 1.0, 'guest_nice': 0.0, 'irq': 0.0, 'iowait': 0.0, 'steal': 0.0, 'system': 0.0, 'guest': 0.0, 'nice': 0.0},
    #    {'softirq': 0.0, 'idle': 100.0, 'user': 0.0, 'guest_nice': 0.0, 'irq': 0.0, 'iowait': 0.0, 'steal': 0.0, 'system': 0.0, 'guest': 0.0, 'nice': 0.0},
    #    {'softirq': 0.0, 'idle': 99.0, 'user': 1.0, 'guest_nice': 0.0, 'irq': 0.0, 'iowait': 0.0, 'steal': 0.0, 'system': 0.0, 'guest': 0.0, 'nice': 0.0}
    #]
    #

def get_cpu_count_logical():
    return psutil.cpu_count(logical=True)

def get_cpu_count_physical():
    return psutil.cpu_count(logical=False)

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
                "total":a.total,
                "available":a.available,
                "percent":a.percent,
                "used":a.used,
                "free":a.free,
                "active":a.active,
                "inactive":a.inactive,
                "buffers":a.buffers,
                "cached":a.cached,
                "shared":a.shared
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
    d={}
    #sdiskusage(total=0, used=0, free=0, percent=0.0)
    for elm in a :
        d[elm['device']]=   {
                                'total':psutil.disk_usage(elm['mountpoint']).total ,
                                'used':psutil.disk_usage(elm['mountpoint']).used ,
                                'free':psutil.disk_usage(elm['mountpoint']).free ,
                                'percent':psutil.disk_usage(elm['mountpoint']).percent
                            }
    return d 
if __name__=="__main__":
    print  get_disk_usage()
