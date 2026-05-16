import psutil

threshold = int(input("Enter the CPU usage in percent :"))

cpu_usage=psutil.cpu_percent(interval=1)

if cpu_usage > threshold: 
    print(f"CPU usage is high: {cpu_usage}%")
else:
    print(f"CPU usage is normal: {cpu_usage}%")


"""
psutil = used for retrieving information on system utilization 
(CPU, memory, disks, network, sensors) and system uptime.
It is a cross-platform library for accessing system details and process utilities.
"""