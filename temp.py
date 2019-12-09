import time

file=''
def choose_file():
    global file
    minute = time.localtime().tm_min/5
    file = str(minute) + '.txt'

print file
