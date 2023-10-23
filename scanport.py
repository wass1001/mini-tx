import socket

def scan_ports(target):
    try:
        targetIP = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid host or unable to resolve host name.")
        return

    print('Starting scan on host: ', targetIP)
    
    open_ports = []

    for port in range(1, 65536):  # Adjust the range as needed
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt
        result = s.connect_ex((targetIP, port))
        if result == 0:
            open_ports.append(port)
            print('Port %d: OPEN' % port)
        s.close()

    if open_ports:
        print('Open ports on', targetIP, ':', open_ports)
    else:
        print('No open ports found on', targetIP)

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    scan_ports(target)
