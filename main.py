#!/usr/bin/env python3

#nehj's extra wallpaper v0.1a ! :D
#main will also process communication with the system separately to avoid frame drop while waiting queries. and Also for holyness

from sub_layer import *; from time import sleep ; from multiprocessing import Process,Pipe ; from os import system

#TO DO LIST:
    #- rays to cursor
    #- grab object 3D
    #- grab object 2D
    #- start the design

def isRunningWhenNotFocused(bool=True):
    if bool:
        return True
    else:
        return False



tick=0
cooldown=0
#add another layer of pipe to delegate os.function
#nw.runInParallel(init_wp_and_run())

parent_connToOS,child_connToOS = Pipe()
p = Process(target=init_wp_and_run, args=(child_connToOS,))
p.start()
data=""

while True:
    sleep(1/12)
    tick+=1
    
    data=parent_connToOS.recv()
        
    if data == "firefox":
        system('nohup firefox')
        system('rm nohup.out')
        data = "flushed"
        
    if data == "kitty":
        system('nohup kitty')
        system('rm nohup.out')
        data = "flushed"

              
    
 



#win,lmb,pos
