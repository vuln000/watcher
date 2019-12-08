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
           # print 'tcp'
            #print str(pkt[IP].src) + ':' + str(pkt[TCP].sport) + '---->' + str(pkt[IP].dst) + ':' + str(pkt[TCP].dport)
            #temp.append(int(time.time()%100000))
            #temp.append(str(pkt[IP].src))
            #temp.append(str(pkt[TCP].sport))
          #  temp.append(str(pkt[IP].dst))
           # temp.append(str(pkt[TCP].dport))
            #temp.append('TCP')
            if get_servers_by_port(pkt[TCP].sport):
                #temp.append(get_servers_by_port(pkt[TCP].sport))
                print(get_servers_by_port(pkt[TCP].sport))
            elif(get_servers_by_port(pkt[TCP].dport)):
                print(get_servers_by_port(pkt[TCP].dport))
            else:
                print 'Unknown'


        if pkt.haslayer('UDP'):
            if get_servers_by_port(pkt[UDP].sport):
                #temp.append(get_servers_by_port(pkt[TCP].sport))
                print(get_servers_by_port(pkt[UDP].sport))
            elif(get_servers_by_port(pkt[UDP].dport)):
                print(get_servers_by_port(pkt[UDP].dport))
            else:
                print 'Unknown'
def get_servers_by_port(sport):#find the servers by port
    try:
        servers = socket.getservbyport(sport)
    except:
        return False
    return servers

def watcher(interface):
    sniff(iface=interface, prn=parse_ip)
watcher('wlan0')