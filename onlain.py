import itertools
from bitcoin import *
import random
import urllib.request
import colorama
import time, threading
from colorama import init
from colorama import init, Fore, Back, Style
init()
print("= Please Enter Desired Search Area =")
a = int(input('Минимальный Диапазон в Bits: '))
b = int(input('Максимальный диапазон Bits: '))
c = int(input('Шаг Bits: '))
print ("================")



def SendSpace():
 while True:

    ran=random.randrange (2**a,2**b,c)
    #ran = random.getrandbits(с)
    #ran = random.randrange(low,high,1)
    myhex = "%064x" % ran
    myhex = myhex[:64]
    priv = myhex
    pub = privtopub(priv)
    pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
    addr = pubtoaddr(pubkey1)
    addr2 = pubtoaddr(pub)

    contents1 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr).read()

    if int (contents1) > 0:
        print(Fore.BLUE + "KEY!","COMPRESSED   BTC:"+ str(contents1.decode('UTF8')),addr,addr2,myhex)
        s1 = myhex
        s2 = addr
        f=open("FOUND BTC.txt","a")
        f.write("address: " + s2 + "\n" + "hex: " + s1 + "\n\n") 
        f.close()
        pass
    contents2 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr2).read()

    if int (contents2) > 0:
        print(Fore.BLUE + "KEY!","UNCOMPRESSED BTC:"+ str(contents2.decode('UTF8')),addr,addr2,myhex)
        s1 = myhex
        s2 = addr2
        f=open("FOUND BTC.txt","a")
        f.write("address: " + s2 + "\n" + "hex: " + s1 + "\n\n") 
        f.close()
        pass
    else:
        
        #http://blockchain.info/q/addressbalance/"
        print(Fore.GREEN +"C:",addr,"U:",addr2,"hex:",myhex)
        print(Fore.RED +"COMPRESSED   BTC:"+ str(contents1.decode('UTF8')))
        print(Fore.RED +"UNCOMPRESSED BTC:"+ str(contents2.decode('UTF8')))
threads = []
for i in range(10):
    t = threading.Thread(target=SendSpace)
    threads.append(t)
    t.start()
