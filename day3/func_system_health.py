import psutil

cpu_threshold = int(input("Enter the CPU usage threshold percentage: " ))

def check_cpu_usage():
    try:
        cpu_usage= psutil.cpu_percent(interval=1)
        if cpu_usage > cpu_threshold:
            print(f"Warning: CPU usage is high at {cpu_usage}%")
        else:
            print(f"CPU usage is normal at {cpu_usage}%")
    except Exception as e:
        print(f"An error occurred while checking CPU usage: {e}")

check_cpu_usage()    
