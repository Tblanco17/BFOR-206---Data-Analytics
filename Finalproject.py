from scapy.all import *

import re
import zlib

pictures_directory = "/home/tyler/scripts/pictures"
faces_directory = "/home/tyler/scripts/faces"
pcap_file = "/home/tyler/scripts/images5.pcap"


mailsniff=sniff(offline="/home/tyler/scripts/images5.pcap", store=True)


numpackets=len(rdpcap("/home/tyler/scripts/images5.pcap"))
print(numpackets) ##Number 1


packettype=rdpcap("/home/tyler/scripts/images5.pcap")
print(packettype) ##Number 2

pkts = rdpcap("/home/tyler/scripts/images5.pcap")
pkts.conversations() ##Number 3

s = mailsniff.sessions() #Number 4

list(s.keys())
s.values
dictionary = {}
i=1

for key, value in s.items():
	dictionary[key]=len(value)

for k in sorted(dictionary, key=lambda k :dictionary[k], reverse=True):
	if i <6:
		print(k, dictionary[k])
		i+=1
	else:
		break

pkt2 = len(sniff(count=5)) #Number 5 Start
print(pkt2)

pkt = sniff(count=5)
print(pkt)

pkt3 = sniff(count=5)
pkt3.conversations()


mailsniff=sniff(count=5, store=True)


s = mailsniff.sessions()

list(s.keys())
s.values
dictionary = {}
i=1

for key, value in s.items():
        dictionary[key]=len(value)

for k in sorted(dictionary, key=lambda k :dictionary[k], reverse=True):
        if i <6:
                print(k, dictionary[k])
                i+=1
        else:
                break

#Number 5 end
##############################4.2$$$$$$$$$$$$$$$$$$$$$

packetss = rdpcap("/home/tyler/scripts/images5.pcap") #4.2 Number 1

for packets in packetss:
	print("Iterating through packets")
	#packetss.summary() Takes forever but delivers the right information
################################http dictioanry part##########
from scapy.all import *  #4.2 Number 2 


def http_header(packet):
        http_packet=str(packet)
        if http_packet.find('GET'):
                return GET_print(packet)

def GET_print(packet1):
        ret = ""
        ret += "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
        ret += ""
        return ret

sniff(offline="/home/tyler/scripts/images5.pcap", prn=http_header, store=True)


print("These are the HTTP Headers saved to the Dictionary")

