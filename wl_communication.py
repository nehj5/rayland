#!/usr/bin/env python3
import evdev
from time import sleep
import socket
from os import popen, system


def get_active_window(child_connToAW): #.3% cpu per 10fps
    #init connection
    sock2_activewindow = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock2_activewindow.setblocking(False)
    socket2_path = popen('echo $XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock').read().strip()
    data_activewindow=""

    print('connecting to %s' % socket2_path)
    try:
        sock2_activewindow.connect(socket2_path)
        print('connected to IPC success')

    except (socket.error):
        print("couldn't get hyprland's IPC access, are you sure your computer is turned on?")
        exit(1)

    #loop fetch data stream

    while True:
        sleep(1/10)
        
        try:
            data_activewindow = sock2_activewindow.recv(1024)
            data_activewindow = data_activewindow.decode('utf-8').strip().replace(" ","[]").replace('\n','{}')
            child_connToAW.send(data_activewindow)
            
        except BlockingIOError:
            pass
            

def get_mouse_press(child_connToLMB): #0.3-1% cpu *2 (for m.down + m.up) # WILL HAVE TO ADD OTHER DEVICES

    devices=[]
    device_list = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in device_list:
        devices.append(evdev.InputDevice(device.path))
    if devices==[]:
        print("couldn't access mouse devices, does user have access to /dev/input/event{{mouse}} ?")

    index=0
    n=0
    while True:
        sleep(1/20)
        
        try:  
            for event in devices[index].read():
                if event != evdev.ecodes.EV_KEY:   
                    #print(event)
                    if str(evdev.categorize(event)).find('ABS_MT_TRACKING_ID') != -1 or str(evdev.categorize(event)).find('589825') != -1: # 589826 for right click ### ADD OTHER DEVICES HERE vvv
                        n+=1
                        eventpass = n
                        child_connToLMB.send(str(eventpass))

        except BlockingIOError:
            child_connToLMB.send(str(" "))
            
        index+=1
        if index>=len(devices):
            index=0


def get_cursor_pos(child_connToCursorPos): #.3-.7cpu at per10fps
    socket_path = popen('echo $XDG_RUNTIME_DIR/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket.sock').read().strip()

    while True:
        sleep(1/20)
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
            client.connect(socket_path)
            client.sendall("cursorpos".encode())
            cursor_pos = client.recv(1024).decode()
            child_connToCursorPos.send(str(cursor_pos))
            
            
#nw.runInParallel(get_active_window,get_mouse_press,get_cursor_pos,)
#nw.run_cpu_tasks_in_parallel([get_active_window,get_mouse_press,get_cursor_pos,]) # really nice performance but can it pipe ? prolly not
