from scapy.all import *
import socket
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
            #print 'tcp'
            #print str(pkt[IP].src) + ':' + str(pkt[TCP].sport) + '---->' + str(pkt[IP].dst) + ':' + str(pkt[TCP].dport)
            temp.append(int(time.time()%100000))
            temp.append(str(pkt[IP].src))
            temp.append(str(pkt[TCP].sport))
            temp.append(str(pkt[IP].dst))
            temp.append(str(pkt[TCP].dport))
            #temp.append('TCP')
            temp.append(get_servers_by_port(pkt[TCP].sport,pkt[TCP].dport))
            print 'tcp   ' + str(pkt[IP].src) + ':' + str(pkt[TCP].sport) + '---->' + str(pkt[IP].dst) + ':' + str(pkt[TCP].dport) + '   ' +str(temp[-1])

        if pkt.haslayer('UDP'):
            #print 'udp'
            temp.append(int(time.time()%100000))
            temp.append(str(pkt[IP].src))
            temp.append(str(pkt[UDP].sport))
            temp.append(str(pkt[IP].dst))
            temp.append(str(pkt[UDP].dport))
            #temp.append('UDP')
            temp.append(get_servers_by_port(pkt[UDP].sport,pkt[UDP].dport))
            print 'udp   ' + str(pkt[IP].src) + ':' + str(pkt[UDP].sport) + '---->' + str(pkt[IP].dst) + ':' + str(pkt[UDP].dport) + '   ' +str(temp[-1])

        if(len(temp)>0):
            write_to_txt(temp)
def get_servers_by_port(sport,dport):#find the servers by port# only concern application ios model for now
    try:
        servers = socket.getservbyport(min(sport,dport))
    except:
        return 'Unknown'
    return servers

def watcher(interface):
    sniff(iface=interface, prn=parse_ip)
watcher('wlan0')