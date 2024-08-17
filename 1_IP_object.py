import scapy.all as scapy
##Basic operation on packet
a=scapy.IP(ttl=10)
print(f"TTL value :{a.ttl}\nSender ip:{a.src} ")
a.dst="123.45.67.88"
print("IP packet a :")
a.show()
del(a.ttl)
print("IP packet After delete TTL :",a.ttl)

##Create packet
ip=scapy.IP()                                   ##When you call IP(), you’re initializing a new IP packet with default values, which can be customized by setting various fields.
print("New IP packet with default values",ip)
ip=scapy.IP(dst="66.66.66.66")                  ##creates an IP packet with the destination address set to 66.66.66.66
print("New IP packet with explicit values",ip)

##Using domain name

target="www.google.com"
ip=scapy.IP(dst=target)
print("New IP packet with domain name ",ip)
print(ip.show())                                ##show all the information of our packet
print(ip.summary())

##creating four packet 
ip=scapy.IP(dst="154.67.87.44/30")
packet=[p for p in ip]
print("Creting four packet ",packet)
print(packet[0],packet[1],packet[2])

##Manipulating some packet

print("Packet information before manipulating :",ip.show())
ip.dst="123.45.67.8"
ip.ttl=46
ip.frag=True
ip.len=222
ip.version=6
print("Packet after manipulating :",ip.show())

##Let’s say I want a broadcast MAC address, and IP payload to google.com and youtube.com to , TTL value(1,200)

packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst=["google.com","youtube.com"],ttl=(1,200))/scapy.UDP()
ans,uans = scapy.srp(packet , timeout=2)   ##srp stand for send and receive packet take packet as agrument that needs to be send and time out after which time out expire 
#we have 400 packet in one line
# Return Values
# ans: This variable contains the packets that received a response. It is a list of tuples where each tuple contains the received response packet and the corresponding sent packet. Essentially, ans includes packets that received replies from the target hosts.
# unans: This variable contains the packets that did not receive a response. It is a list of tuples where each tuple contains the sent packet that did not get a reply.
print("Answered packets:")
for sent_packet, received_packet in ans:
     print(f"Sent: {sent_packet.summary()}")
     print(f"Received: {received_packet.summary()}")








