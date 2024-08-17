import scapy.all as scapy
a=scapy.IP()
print("Packet with default value :",a)
a=scapy.IP()/scapy.TCP()
print(a)                                       ## output is source ip and port & destination ip and post
a=scapy.Ether()/scapy.IP()/scapy.TCP()
print("Ether ,IP ,TCP, in Header :")
print(a.show())
a=scapy.Ether()/scapy.IP()/scapy.TCP()/"Rohti"     ##TCP send Rohit as raw data
print(a)
print("Ether ,IP ,TCP,RAW Data :")
print(a.show())
a=scapy.Ether()/scapy.IP()/scapy.UDP()
print("Ether ,IP ,UDP:")
print(a.show())
a=scapy.Ether()/scapy.IP()/scapy.IP()/scapy.UDP()
print("Ether , IP,IP,UDP header :")
print(a.show())
a=scapy.IP(proto=55)/scapy.TCP()
print(" IP(proto=55),TCP header :")
print(a.show())

##representing of packet in hexadecimal 
ip=scapy.raw(scapy.IP())                                                ## raw() used to represent in hexa
print("Representation of IP header in Hexa decimal form",ip)
tcp=scapy.raw(scapy.TCP())
print("Representation of TCP header in Hexa decimal form",tcp)
a=scapy.Ether()/scapy.IP(dst="www.slashdot.org")/scapy.TCP()/"GET /index.html HTTP/1.0 \n\n"
print(a)
print("Haxdump : ")
scapy.hexdump(a)
b=scapy.raw(a)                                                         ### Convert the packet 'a' to raw byte string.
print("Hexa decimal using raw(): ")
print("b:",b)
c=scapy.Ether(b)                                   ### Interpret the raw bytes as an Ethernet frame back to the readable form 
print("Interpret ' b ' as Ether net frame",c)
c=scapy.IP(b)                                     ### Interpret the raw bytes as an IP Packet back to readable form 
print("Interpret ' b 'as Ip Packet :",c)
c=scapy.Ether(b)
print("Packet without hide_defaults()")
print(c)
c.hide_defaults()                       ## normally used to hide default value
print("Packet with hide_defaults()")
print(c)
