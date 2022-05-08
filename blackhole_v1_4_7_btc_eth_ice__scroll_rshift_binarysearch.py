from multiprocessing import Pool
from threading import Thread
import secp256k1 as ice
import numpy as np
import random
import os
import time
hashlist = np.fromfile('btc1sortold.bin',dtype=np.uint8)
b = int(len(hashlist)/20)
hashlist.shape = (b,20)
hashlist_b = hashlist[:,0:6]
ethlist = np.fromfile('ethaddrsort.bin',dtype=np.uint8)
bb = int(len(ethlist)/20)
ethlist.shape = (bb,20)
ethlist_b = ethlist[:,0:6]
def addruncomp(pvkey,maxbuf):
        addruncomp_arr = np.frombuffer(ice.privatekey_loop_h160 (maxbuf,0, False,pvkey),dtype=np.uint8)
        addruncomp_arr.shape=(maxbuf,20)
        addruncomp_arr_b = addruncomp_arr[:,0:6]
        index2 = 0
        while index2 <= len(addruncomp_arr_b)-1:
                first = 0
                last = len(hashlist_b)-1
                index = -1
                while (first <= last) and (index == -1):
                        mid = int((first  + last)// 2)
                        if  bytes(addruncomp_arr_b[index2]) == bytes(hashlist_b[mid]):
                                if  bytes(addruncomp_arr[index2]) == bytes(hashlist[mid]):
                                        file = open('result100_uncom.txt','a+')
                                        file.write (f"{hex(pvkey+index2)[2:].zfill(64)};{bytes(addruncomp_arr[index2]).hex()};{bytes(hashlist[mid]).hex()};\n")
                                        print (f"Fount RMD160 uncomp addr 100% {hex(pvkey+index2)[2:].zfill(64)};{bytes(addruncomp_arr[index2]).hex()};{bytes(hashlist[mid]).hex()}\n")
                                        file.close()
                                        break
                                file = open('result_uncom.txt','a+')
                                file.write (f"{hex(pvkey+index2)[2:].zfill(64)};{bytes(addruncomp_arr[index2]).hex()};{bytes(hashlist[mid]).hex()};\n")
                                print (f"Fount RMD160 uncomp addr >25% {hex(pvkey+index2)[2:].zfill(64)};{bytes(addruncomp_arr[index2]).hex()};{bytes(hashlist[mid]).hex()}\n")
                                file.close()
                                break
                        else:
                                if bytes(addruncomp_arr_b[index2]) < bytes(hashlist_b[mid]):
                                        last = mid -1
                                else:
                                        first = mid +1
                index2 +=1
def addrcomp(pvkey,maxbuf):
        addrcomp_arr = np.frombuffer(ice.privatekey_loop_h160 (maxbuf,0, True,pvkey),dtype=np.uint8)
        addrcomp_arr.shape=(maxbuf,20)
        addrcomp_arr_b = addrcomp_arr[:,0:6]
        index2 = 0
        while index2 <= len(addrcomp_arr_b)-1:
                first = 0
                last = len(hashlist_b)-1
                index = -1
                while (first <= last) and (index == -1):
                        mid = int((first  + last)// 2)
                        if  bytes(addrcomp_arr_b[index2]) == bytes(hashlist_b[mid]):
                                if  bytes(addrcomp_arr[index2]) == bytes(hashlist[mid]):
                                        file = open('result100_com.txt','a+')
                                        file.write (f"{hex(pvkey+index2)[2:].zfill(64)};{bytes(addrcomp_arr[index2]).hex()};{bytes(hashlist[mid]).hex()};\n")
                                        print (f"Fount RMD160 comp addr 100% {hex(pvkey+index2)[2:].zfill(64)};{bytes(addrcomp_arr[index2]).hex()};{bytes(hashlist[mid]).hex()}\n")
                                        file.close()
                                        break
                                file = open('result_com.txt','a+')
                                file.write (f"{hex(pvkey+index2)[2:].zfill(64)};{bytes(addrcomp_arr[index2]).hex()};{bytes(hashlist[mid]).hex()};\n")
                                print (f"Fount RMD160 comp addr >25% {hex(pvkey+index2)[2:].zfill(64)};{bytes(addrcomp_arr[index2]).hex()};{bytes(hashlist[mid]).hex()}\n")
                                file.close()
                                break
                        else:
                                if bytes(addrcomp_arr_b[index2]) < bytes(hashlist_b[mid]):
                                        last = mid -1
                                else:
                                        first = mid +1
                index2 +=1
def ethcomp(pvkey,maxbuf):
        ethcomp_arr = np.frombuffer(ice.privatekey_group_to_ETH_address_bytes (pvkey,maxbuf),dtype=np.uint8)
        ethcomp_arr.shape=(maxbuf,20)
        ethcomp_arr_b = ethcomp_arr[:,0:6]
        index2 = 0
        while index2 <= len(ethcomp_arr_b)-1:
                first = 0
                last = len(ethlist_b)-1
                index = -1
                while (first <= last) and (index == -1):
                        mid = int((first  + last)// 2)
                        if  bytes(ethcomp_arr_b[index2]) == bytes(ethlist_b[mid]):
                                if  bytes(ethcomp_arr[index2]) == bytes(ethlist[mid]):
                                        file = open('result100_eth.txt','a+')
                                        file.write (f"{hex(pvkey+index2)[2:].zfill(64)};{bytes(ethcomp_arr[index2]).hex()};{bytes(ethlist[mid]).hex()};\n")
                                        print (f"Fount Eth addr 100% {hex(pvkey+index2)[2:].zfill(64)};{bytes(ethcomp_arr[index2]).hex()};{bytes(ethlist[mid]).hex()}\n")
                                        file.close()
                                        break
                                file = open('result_eth.txt','a+')
                                file.write (f"{hex(pvkey+index2)[2:].zfill(64)};{bytes(ethcomp_arr[index2]).hex()};{bytes(ethlist[mid]).hex()};\n")
                                print (f"Fount Eth addr >25% {hex(pvkey+index2)[2:].zfill(64)};{bytes(ethcomp_arr[index2]).hex()};{bytes(ethlist[mid]).hex()}\n")
                                file.close()
                                break
                        else:
                                if bytes(ethcomp_arr_b[index2]) < bytes(ethlist_b[mid]):
                                        last = mid -1
                                else:
                                        first = mid +1
                index2 +=1
                
def core(prg_list):     

        f = open('high.txt', 'r')
        for line in f:
            highrange = int(line,16)
        f.close()
        f = open('low.txt', 'r')
        for line in f:
            lowrange = int(line,16)
        f.close()
        maxbuf = 0xffff#int(input('Maximum number of generation:'))
        t = [None] * 6
        progress = 0
        while progress < 10000:
                point = random.randrange(lowrange,highrange)
                strpoint = str(bin(point)[2:-int(len(str(bin(maxbuf)[2:])))])
                for i in range(1, int(len(strpoint)), 1):
                        strpoint2 = strpoint[-i:] + strpoint[:-i]
                        strpoint2 = strpoint2.ljust(int(len(strpoint2)+len(str(bin(maxbuf)[2:]))),"0")
                        scrolladdr = int(strpoint2,2)
                        if scrolladdr > lowrange and scrolladdr < highrange:
                                t[0] = Thread(target=addruncomp, args=(scrolladdr,maxbuf))
                                t[1] = Thread(target=addrcomp, args=(scrolladdr,maxbuf))
                                t[2] = Thread(target=ethcomp, args=(scrolladdr,maxbuf))
                                t[0].start()
                                t[1].start()
                                t[2].start()
                                t[0].join()
                                t[1].join()
                                t[2].join()
                                progress = progress + maxbuf
                                print (f"Scroll point:{hex(scrolladdr)[2:].zfill(64)} {hex(scrolladdr+maxbuf)[2:].zfill(64)}")
                        rshift = int(strpoint[:-i].ljust(int(len(strpoint[:-i])+len(str(bin(maxbuf)[2:]))),"0"),2)
                        if rshift > lowrange and rshift < highrange and rshift != scrolladdr:
                                t[3] = Thread(target=addruncomp, args=(rshift,maxbuf))
                                t[4] = Thread(target=addrcomp, args=(rshift,maxbuf))
                                t[5] = Thread(target=ethcomp, args=(rshift,maxbuf))
                                t[3].start()
                                t[4].start()
                                t[5].start()
                                t[3].join()
                                t[4].join()
                                t[5].join()
                                progress = progress + maxbuf
                                print (f"Rshift point:{hex(rshift)[2:].zfill(64)} {hex(rshift+maxbuf)[2:].zfill(64)}")
        return progress
if __name__ == '__main__':
        prg = 0
        processes = int(input('Input number of processes:'))
        prg_list = [0] * processes
        while True:
                progress_time = time.time()
                pool = Pool(processes)
                progress = sum(pool.map(core,prg_list))
                pool.close()
                progress_time = time.time() - progress_time
                prg = prg + progress
                print(f"Speed {progress//int(progress_time)} Keys/sec  - total scaned:{prg}")

                        

# You can send your suggestions and suggestions for the script
# https://t.me/gsxde
