import pandas as pd
import matplotlib.pylab as plt
import time
email_addr = '237834893@qq.com'
alpha = 1000
plt.ion()
#fig, ax = plt.subplots(3, 1)
file = 'a.txt'

def choose_file():# could update for optimal cpu using
    global file
    minute = time.localtime().tm_min / 5
    file = 'data/' + str(minute) + '.txt'
    #print file

def plot_stream():
    global file
    choose_file()
    plt.clf()

    data =pd.read_csv(file)
    data.columns=['time','ip_src','port_src','ip_dst','port_dst','protocol','n']
    del data['n']

    #io graph start
    io = data['time'].value_counts(sort=False,ascending=True)
    if(sum(io[-5:-1])>alpha):        #whilee sum of the last five seconds exceed alpha,send a alert email or smb message
        try:
            send_alert_email(sum(io[-5:-1]))
        except:
            send_alert_smb(sum(io[-5:-1]))
    io = io.sort_index(ascending=True)
    graph_io = plt.subplot(3, 2, 1)
    graph_io.set_xlabel('time',fontsize=10)
    graph_io.set_ylabel('packet per seconds', fontsize=10)
    graph_io.plot(io)

    graph_io.spines['top'].set_visible(False)
    graph_io.spines['right'].set_visible(False)
    graph_io.spines['bottom'].set_visible(False)
    graph_io.spines['left'].set_visible(False)

    ##print io
    #io graph end
    sent = data['ip_src'].value_counts()[0:5] #user sent
    graph_sent = plt.subplot(3, 2, 3)
    graph_sent.set_xlabel('user_ip',fontsize=10)
    graph_sent.set_ylabel('sent_number', fontsize=10)
    graph_sent.bar(sent.index,sent,color='c')
    graph_sent.spines['top'].set_visible(False)
    graph_sent.spines['right'].set_visible(False)
    graph_sent.spines['bottom'].set_visible(False)
    graph_sent.spines['left'].set_visible(False)

    recv = data['ip_dst'].value_counts()[0:5] #user_recv
    graph_recv = plt.subplot(3, 2, 5)
    graph_recv.set_xlabel('user_ip',fontsize=10)
    graph_recv.set_ylabel('recv_number', fontsize=10)
    graph_recv.bar(recv.index,recv,color='g')
    graph_recv.spines['top'].set_visible(False)
    graph_recv.spines['right'].set_visible(False)
    graph_recv.spines['bottom'].set_visible(False)
    graph_recv.spines['left'].set_visible(False)

    port_src = data['port_src'].value_counts()[0:7]#port_src_pie
    graph_port_src = plt.subplot(2,2,2)
    graph_port_src.pie(port_src,labels=port_src.index,autopct='%1.1f%%')

    protocol = data['protocol'].value_counts()[0:7]#protocal_dst_pie
    graph_port_dst = plt.subplot(2,2,4)
    graph_port_dst.pie(protocol,labels=protocol.index,autopct='%1.1f%%')

    #plt.draw()
    plt.pause(0.1)
def send_alert_email(a):
    try:
        #send..email..here
        print "send"
        return True
    except:
        print"send alert email failed try to send smb message"
        return False
def send_alert_smb(a):
    try:
        #send..messagge..here
        print "send"
        return True
    except:
        print"send alert email failed try to send smb message"
        return False
while True:
    plot_stream()
    #time.sleep(3)
