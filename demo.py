from scapy.all import *

file = 'a.txt'
def write_to_txt(data):
    with open(file,'a+') as f:
        for i in data:
            f.write(str(i)+',')
        f.write('\n')

def parse_ip(pkt):
    temp = []
    if pkt.haslayer('IP'):#ipv4 for now
        if pkt.haslayer('TCP'):
            print 'tcp'
            print str(pkt[IP].src) + ':' + str(pkt[TCP].sport) + '---->' + str(pkt[IP].dst) + ':' + str(pkt[TCP].dport)
            temp.append(int(time.time()%100000))
            temp.append(str(pkt[IP].src))
            temp.append(str(pkt[TCP].sport))
            temp.append(str(pkt[IP].dst))
            temp.append(str(pkt[TCP].dport))
            temp.append('TCP')

        if pkt.haslayer('UDP'):
            print 'udp'
            print str(pkt[IP].src) + ':' + str(pkt[UDP].sport) + '---->' + str(pkt[IP].dst) + ':' + str(pkt[UDP].dport)
            temp.append(int(time.time()%100000))
            temp.append(str(pkt[IP].src))
            temp.append(str(pkt[UDP].sport))
            temp.append(str(pkt[IP].dst))
            temp.append(str(pkt[UDP].dport))
            temp.append('UDP')
        if(len(temp)>0):
            write_to_txt(temp)

def watcher(interface):
    sniff(iface=interface, prn=parse_ip)
watcher('wlan0')