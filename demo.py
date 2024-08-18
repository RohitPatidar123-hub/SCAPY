from  scapy.all import *
p = scapy.sr1(scapy.Ether()/scapy.IP(ttl=(1,5))/scapy.ICMP()/"XYZ") ##sends an ICMP Echo Request packet with a payload to the specified destination and waits for a single response.
if p:
    print("Response")
else: 
    print("No response ")
        