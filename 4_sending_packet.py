from  scapy.all import *

################Sending Packet ####################
print("Send packet at layer 2:")
send(IP(dst="1.2.3.4")/ICMP())                            ##this create packet as well as send packet at layer 2 ip 
print("\nSend packet at layer 3 :")
sendp(Ether()/IP(dst="1.2.3.4",ttl=(1,4)), iface=None,)   ##this create packet as well as send packet at layer 3 
##sendp("I'm travelling on Ethernet", iface="eth1", loop=1, inter=0.2)   ## infinite loop
# ##l=sendp(rdpcap("C:\\Users\\rohit\\Downloads\\speedtest.pcapng"))    ##read packet from pcap file and send and return no. of packet send successful
# ##print(l)
l=send(IP(dst="23.43.54.3") , return_packets=True)  ##along with send it  return  packet list that are send successfully 
print("Send pcaket at layer 2",l)
a=sendp(Ether()/IP()/fuzz(TCP()/UDP()/NTP(version =4 )/"rohit"),return_packets=True) ## fuzz function is used to apply random modifications to the UDP/NTP packet. This is useful for testing the robustness of the target system against unexpected or malformed packet data
print("Send icmp packet at layer 3 :",a)
p = sr1(IP(dst="www.slashdot.org")/ICMP()/"XYZ")  ##sends an ICMP Echo Request packet with a payload to the specified destination and waits for a single response.
print("Sending data through sr1():",p)      ##sr1 is return single response of packet
print(p.show())
ans,unans=sr(IP()/TCP()/UDP()/"Rohit",inter=1,retry=-2)  ##send packet and  receive response for all packet 
print("sending packet through sr():")                    ##time between two consicutive packet ,retry means no of times unanswered packet send till time out 
print(ans.summary())                                    
print(unans)

p=sr1(IP(dst="www.google.com")/TCP(dport=80,flags="S"))    #initiate communication by sewtting flags=s
print(p.show())
p=sr(IP(dst="192.168.1.1")/TCP(sport=666,dport=(440,443),flags="S")) 
print(p)
p=sr(IP(dst="192.168.1.1")/TCP(sport=RandShort(),dport=[440,441,442,443],flags="S"))
print(p)

