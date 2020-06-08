import socket

group = '239.195.140.6'
port = 49006
bind = '0.0.0.0'
source = '91.203.255.242'

if __name__ == "__main__":
    if not hasattr(socket, 'IP_ADD_SOURCE_MEMBERSHIP'):
        setattr(socket, 'IP_ADD_SOURCE_MEMBERSHIP', 39)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    imr = (socket.inet_pton(socket.AF_INET, group) + socket.inet_pton(socket.AF_INET, bind) + socket.inet_pton(
        socket.AF_INET, source))

    s.setsockopt(socket.IPPROTO_IP, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_SOURCE_MEMBERSHIP, imr)
    s.bind((group, port))

    while True:
        print("Listen")
        msg = s.recv(256)
        print(msg)
