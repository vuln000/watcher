# -*- coding:utf-8 -*-

import sys
import os

target = sys.argv[1]
os.system('iptables -I INPUT -s '+target+' -j DROP')
print target+' has been banned'
#iptables -L INPUT –line-numbers 
#iptables -D INPUT 1
#
