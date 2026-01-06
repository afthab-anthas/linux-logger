
import time
import subprocess
from datetime import datetime

# CONFIGURATION
LOG_FILE = "/home/admin/repos/linux-logger/process_log.txt"

def get_top_processes():
    # We use the native 'ps' command to avoid installing external libraries.
    # -e: all processes
    # -o: output specific columns
    # --sort: sort by cpu usage (descending)
    cmd = "ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 6"
    
    try:
        # Run the command and grab output
        result = subprocess.check_output(cmd, shell=True).decode("utf-8")
        return result
    except subprocess.CalledProcessError as e:
        return f"Error fetching processes: {e}"

def main():
    print("Service Started...")
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = get_top_processes()
        
        entry = f"--- SNAPSHOT AT {timestamp} ---\n{data}\n"
        
        # 'a' mode appends to the file instead of overwriting
        with open(LOG_FILE, "a") as f:
            f.write(entry)
            
        # Sleep for 2 seconds
        time.sleep(2)

if __name__ == "__main__":
    main()
