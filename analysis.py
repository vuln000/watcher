import pandas as pd
import matplotlib.pylab as plt
import time

plt.ion()
#fig, ax = plt.subplots(3, 1)
file = 'a.txt'
def plot_stream(file):
    plt.clf()

    data =pd.read_csv('a.txt')
    data.columns=['time','ip_src','port_src','ip_dst','port_dst','porto','n']
    del data['n']

    #io graph start
    io = data['time'].value_counts(sort=False,ascending=True)
    io = io.sort_index(ascending=True)
    graph_io = plt.subplot(3, 2, 1)
    graph_io.set_xlabel('time',fontsize=10)
    graph_io.set_ylabel('number', fontsize=10)
    graph_io.plot(io)
    ##print io
    #io graph end
    sent = data['ip_src'].value_counts()[0:5] #user sent
    graph_sent = plt.subplot(3, 2, 3)
    graph_sent.set_xlabel('user_ip',fontsize=10)
    graph_sent.set_ylabel('sent_number', fontsize=10)
    graph_sent.bar(sent.index,sent)

    recv = data['ip_dst'].value_counts()[0:5] #user_recv
    graph_recv = plt.subplot(3, 2, 5)
    graph_recv.set_xlabel('user_ip',fontsize=10)
    graph_recv.set_ylabel('recv_number', fontsize=10)
    graph_recv.bar(sent.index,recv)

    port_src = data['port_src'].value_counts()[0:10]
    graph_port_src = plt.subplot(2,2,2)
    graph_port_src.pie(port_src)

    port_dst = data['port_dst'].value_counts()[0:10]
    graph_port_dst = plt.subplot(2,2,4)
    graph_port_dst.pie(port_dst)
    #plt.draw()
    plt.pause(0.1)

while True:
    plot_stream(file)
    #time.sleep(3)