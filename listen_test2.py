import socket
import struct

MCAST_GRP = '239.195.140.6'
MCAST_PORT = 49006
HOST = '192.168.255.2'

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((MCAST_GRP, MCAST_PORT))
    sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,
                    socket.inet_aton(MCAST_GRP) + socket.inet_aton(HOST))
    while True:
        print(sock.recv(1024))
