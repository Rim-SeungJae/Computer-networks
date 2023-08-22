# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:14:43 2021

@author: dipreez
"""

import sys
import threading
import time

start = time.time()

def copy(src,dest):
    with open("log.txt",'a') as fp:
        cur_time = time.time() - start
        fp.write(f'{cur_time:.2f}'+"\t"+"Start copying "+src+" to "+dest+"\n")
    with open(src,'rb') as fp1:
        with open(dest,'ab') as fp2:
            while(True):
                buffer = fp1.read(10000)
                if not buffer:
                    break
                fp2.write(buffer)
    with open("log.txt",'a') as fp:
        cur_time = time.time() - start
        fp.write(f'{cur_time:.2f}'+"\t"+dest+" is copied completely"+"\n")


while(True):
    src = input("input the file name: ")
    if src == "exit":
        sys.exit(0)
    dest = input("input the new name: ")
    if dest == "exit":
        sys.exit(0)
    print()
    
    thread = threading.Thread(target=copy, args=(src,dest,))
    thread.start()