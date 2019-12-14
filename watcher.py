from scapy.all import *
import socket
import time
import os
file = 'a.txt'#temp postion
begin_time = time.time()

def init(interface):
    for i in range(12):
        file_path = os.getcwd() + '/data/' + str(i) + '.txt'
        if os.path.isfile(file_path):
            pass
        else:
            os.system('touch ' + file_path)
    if os.system('sudo ifconfig '+str(interface) +' promisc')==0:
        print 'interface mode promisc up, starting watching from system time '+ str(begin_time)
    else:
        print 'interface mode promisc failed,please cheak your interface name and system permissions'
    
def write_to_txt(data):
    with open(file,'a+') as f:
        for i in data:
            f.write(str(i)+',')
        f.write('\n')

def choose_file():# could update for optimal cpu using
    global file
    minute = time.localtime().tm_min / 5
    if  minute == 11:
        next = 0
    else:
        next = minute + 1
    file = 'data/' + str(minute) + '.txt'
    next_file = 'data/' + str(next) + '.txt'
    try:
        with open(next_file,'r+') as f:
            f.truncate()
    except:
        pass
    #print file

def parse_ip(pkt):
    choose_file()
    temp = []
    if pkt.haslayer('IP'):#ipv4 for now
        if pkt.haslayer('TCP'):
            #print 'tcp'
            #print str(pkt[IP].src) + ':' + str(pkt[TCP].sport) + '---->' + str(pkt[IP].dst) + ':' + str(pkt[TCP].dport)
            temp.append(int(time.time()-begin_time))
            temp.append(str(pkt[IP].src))
            temp.append(str(pkt[TCP].sport))
            temp.append(str(pkt[IP].dst))
            temp.append(str(pkt[TCP].dport))
            #temp.append('TCP')
            temp.append(get_servers_by_port(pkt[TCP].sport,pkt[TCP].dport))
            print 'tcp   ' + str(pkt[IP].src) + ':' + str(pkt[TCP].sport) + '---->' + str(pkt[IP].dst) + ':' + str(pkt[TCP].dport) + '   ' +str(temp[-1])

        if pkt.haslayer('UDP'):
            #print 'udp'
            temp.append(int(time.time()-begin_time))
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
    init(interface)
    sniff(iface=interface, prn=parse_ip)
watcher('wlan0')
