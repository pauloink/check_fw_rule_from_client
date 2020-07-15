import socket
import os
import sys

destinations_ = [] 
tcp_ports_ =    #integer value
list_ = open("Result.txt", "w+")
path_ = os.getcwd()

print("SCRIPT RUNNING, PLEASE WAIT...")
for destination, tcp_port in zip(destinations_, tcp_ports_):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    return_ = s.connect_ex((destination, tcp_port))
    s.settimeout(None)

    if return_ == 0:
        list_.write("%s:%s  \tOPEN\r" % (destination, tcp_port))
        s.shutdown(socket.SHUT_WR)
        s.close()
    elif return_ == 10061:
        list_.write("%s:%s  \tSERVER REFUSING CONECTION\r" % (destination, tcp_port))
    elif return_ == 10060:
        list_.write("%s:%s  \tCONECTION NOT STABLISHED. FIREWALL RULE ?\r" % (destination, tcp_port))
    else:
        list_.write("%s:%s  \tCONECTION NOT STABLISHED. FIREWALL RULE ?\r" % (destination, tcp_port))
list_.close()

if sys.platform == "win32":
    print("Finished!!! Data saved on file %s\Result.txt" % path_)
else:
    print("Finished!!! Data saved on file %s/Result.txt" % path_)
