import socket
import time
from tqdm import tqdm

def knock_ports(ip, ports):
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            try:
                s.connect((ip, port))
            except socket.error:
                pass

def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in tqdm(range(start_port, end_port + 1), desc=f"Scanning ports for {ip}", unit="port"):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                # Save the open port in real-time to a text file
                with open(f"realtime_results_{ip}.txt", "a") as real_time_file:
                    real_time_file.write(f"Open port found for {ip}: {port}\n")
    return open_ports

def save_results(ip, open_ports, path="."):
    result_file_path = f"{path}/port_scan_results_{ip}.txt"
    with open(result_file_path, "w") as result_file:
        result_file.write(f"Open ports for {ip}: {open_ports}")

# Fancy script name display
script_name = r"""

 ____  __.                     __      ____  __.                     __    
|    |/ _| ____   ____   ____ |  | __ |    |/ _| ____   ____   ____ |  | __
|      <  /    \ /  _ \_/ ___\|  |/ / |      <  /    \ /  _ \_/ ___\|  |/ /
|    |  \|   |  (  <_> )  \___|    <  |    |  \|   |  (  <_> )  \___|    < 
|____|__ \___|  /\____/ \___  >__|_ \ |____|__ \___|  /\____/ \___  >__|_ \
        \/    \/            \/     \/         \/    \/            \/     \/

"""

# Author
author = "Author: MrMagic0"
print(script_name)
print(author)

# Example usage:
knock_sequence = [1000, 2000, 3000]  # Replace with your desired sequence

# Read IP addresses from a file
ip_file_path = input("Enter the path to the file containing IP addresses: ")
with open(ip_file_path, "r") as ip_file:
    ip_addresses = [line.strip() for line in ip_file]

# Input range of ports to scan
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port:"))

# Loop through each IP address and perform port knocking and scanning
for target_ip in ip_addresses:
    # Knock the ports
    knock_ports(target_ip, knock_sequence)

    # Wait for a moment to simulate a delay
    time.sleep(2)

    # Scan the ports after knocking
    open_ports = scan_ports(target_ip, start_port, end_port)

    # Save the final results to a text file
    save_results(target_ip, open_ports)
