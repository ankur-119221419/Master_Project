import sys
from scapy.all import *

# Filter network traffic with ECN flag
def parse_packet(packet):
	flag=packet['TCP'].flags
	if flag == 0x40:
	   character = chr(packet['TCP'].sport)
	   sys.stdout.write(character)

# Listen to incoming traffic
sniff(filter="tcp", prn=parse_packet)
