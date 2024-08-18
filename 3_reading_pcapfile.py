from  scapy.all import *

import pyx
import reportlab
from PIL import Image

print("PyX version:", pyx.__version__)
print("ReportLab version:", reportlab.Version)
print("Pillow version:", Image.__version__)

A=rdpcap("C:\\Users\\rohit\\Downloads\\speedtest.pcapng")
print(A)
b=PacketList(A)
print(b)
#a[423].pdfdump("output.pdf",layer_shift=1)
#a[423].psdump("output.eps",layer_shift=1)
print(len(A[423]))                          ##size of packet a[423]
a=scapy.IP(dst="www.google.com/30")
print(a.show())
b=[p for p in a]
print(b)                             #
c=scapy.IP(ttl=[1,2,{4,5,6,7,7},(4,5)]) 
print("We can fill field with multiple value :")   ##we can fill field with multiple value
print(c.show())
b=[p for p in c]
print("We can also expand independetly also : ")                     ##we can also expand independently also for eack ttl
print(b)
e=scapy.TCP(dport=[4,453])
b=[p for p in a/e]
print("Total 8 packet :")
print(b)
a=PacketList(b)
print(a)



