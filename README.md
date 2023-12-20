> [!NOTE]
> In the event of improper use of the provided code, I disclaim all responsibility.

> [!IMPORTANT]
> Allow me to remind you that this code is compatible with and can be utilized on both Windows and Linux operating systems.

> [!WARNING]
> This code is intended solely for pedagogical and educational purposes.

This code is a simple port scanner in Python. Here’s what each part does:

***scan_port(ip, port)*** 
> The function attempts to establish a TCP connection to a specific port on a given IP address. It creates a new socket and    
  sets a timeout of 5 seconds for the connect operation. Then, it tries to connect to the specified port on the given IP 
  address. If the connection is successfully established (i.e., ***result == 0***), the port is open. If the connection fails, 
  the port is not open.

***main()***
> The function coordinates the port scanning. It asks the user to input an IP address to scan. Then, it creates a thread pool 
  using ***concurrent.futures.ThreadPoolExecutor*** and submits tasks to this thread pool to scan each port in the range of 1 
  to 65535. As tasks complete, it prints the results. Finally, it prints the total time the scan took.

> This line ensures that the main() function only runs if the script is run directly (i.e., not imported as a module in 
  another script).

> Therefore, this script can be used to determine which ports are open on a given machine, which is useful for security 
  testing and network troubleshooting. However, keep in mind that port scanning can be seen as aggressive behavior by some 
  systems and networks, and may be against acceptable use policies on some networks. Therefore, you should only use this 
  script to scan machines and networks for which you have permission to do so.
