# Master_Project
## Network Covert Channel

### **Description:**
This implementation of Covert Channel is based on TCP header fields and developed using Python language. The client script reads content from a local file on the machine and encodes it into its equivalent ASCII decimal value. Then a TCP packet is crafted with the source port containing the decimal value as input, on the other machine server script monitors the network traffic and any packet with ECN flag set to "E" is captured. Source port value is read and decoded back to its original ASCII value and displayed on the command prompt. 

### **Scripts:**
- client.py - Developed to transmit covert data to server using source port field value.
- server.py - Developed to sniff network traffic and filter covert data received from client. 

### **Usage:**
- Run client script using following command:- python client.py host_IP_Address
- Run server script using following command:- python server.py 

### **Requirements:**
- Python 2.7.x or 3.8.x must be installed. https://www.python.org/downloads/
- Scapy 2.4.x should also be installed before running the scripts. https://scapy.net/download/
- Run both the scripts as root/super user.

