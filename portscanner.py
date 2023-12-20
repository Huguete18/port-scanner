import socket
import time
import concurrent.futures


def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((ip, port))
    if result == 0:
        return f"Port is open: {port}"
    else:
        return f"Port is not open: {port}"


def main():
    ip = input("Enter the ip address: ")
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {
            executor.submit(scan_port, ip, port): port for port in range(1, 65535)
        }
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
