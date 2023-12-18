import socket

ip = input("Enter the ip address:")

for port in range(1, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    
    result = sock.connect_ex((ip, port))
    
    if result == 0:
        print("Port is open: " + str(port))
        sock.close()
    else:
        print("Port is not open: " + str(port))
        sock.close()