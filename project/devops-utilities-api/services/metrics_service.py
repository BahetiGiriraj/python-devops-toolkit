import psutil

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    cpu_threshold = 80.0
    if cpu_usage > cpu_threshold:
        print(f"Warning: CPU usage is high at {cpu_usage}%")
    else:
        print(f"CPU usage is normal at {cpu_usage}%")

    # print(f"Memory usage: {memory_info}%")
    # print(f"Disk usage: {disk_usage}%")
    return {
        "cpu_usage": cpu_usage,
        "memory_total": memory_info,
        "disk_total": disk_usage
    }
    

get_system_metrics()