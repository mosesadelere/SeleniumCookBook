import socket
import os

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      #ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', inter[:15]))[20:24])
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return str(e)

def main():
    portList = [21, 22, 25, 80, 110, 443]
    for ipList in range(1,255):
        ip = "192.168.95." + str(ipList)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print("[+] " + ip + " @ port " + str(port) + " : " + banner)
        if ipList == 15:
            break

if __name__ == '__main__':
    main()