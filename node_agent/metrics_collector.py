import psutil

def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().used
    disk_io = psutil.disk_io_counters().read_bytes
    net_io = psutil.net_io_counters().bytes_sent
    return [cpu, memory, disk_io, net_io]
