#!/usr/bin/env python3

# init
###############################################################################################################################################################################################

# Libraries
from pyray import *; from raylib import *; from math import cos, sin; from nehj_wallpaper_custom_library import * ; from wl_communication import *; from multiprocessing import Process,Pipe; from time import sleep
from init_window import *; from wpEngine import *

#$

def init_wp_and_run(child_connToOS):

# def vars
    sleep(.1)
    isRunningWhenNotFocused = True
    tick=0
    # init vars to not proc error on frame 0, do not worry about it too much just init all vars here
    is_active_window_fullscreen=''; hyprctl_clients_request=""; throttle_clickAmountFor=0;cancel_click_timer = 0; isWpFocused= False; active_window_id=""; active_window_pos=[0,0,0,0]; cooldown_aw=0; isShouldDragCD=0; last_press=0; initDraggingTimer=0; isinitDragging=0; dt=0; init_once = 0; cooldown_lmb=0; unload_lmb=0; is_lmbClicking=False; isDragging=False; cancel_click_timer = 99999999; cursor_pos=Vector2(); ray=Ray(); active_window=""; mouse_clicks=" "

    # init win,cam and graphical assets
    win = Window()
    win.load_window()

    camera = CameraObj()
    camera.init_camera()


# pipes
#########################################################################################################################################################################################################################################################################################
    # pipes
    # DO NOT TOUCH THE PIPES PLEASE FOR THE LOVE OF GOD
    parent_connToAW,child_connToAW = Pipe()
    p1 = Process(target=get_active_window, args=(child_connToAW,))

    parent_connToLMB,child_connToLMB = Pipe()
    p2 = Process(target=get_mouse_press, args=(child_connToLMB,))

    parent_connToCursorPos,child_connToCursorPos = Pipe()
    p3 = Process(target=get_cursor_pos, args=(child_connToCursorPos,))
    p1.start(); p2.start(); p3.start()
    # safe zone from here

# init scene
##############################################################################################################################################################################################################################################################################################


    ##-----referencing assets
    scene_loader = SceneLoader()

# start main loop
#########################################################################################################################################################################################################################################################

    isRunning=True
    while isRunning==True:


#§
# receive data and manages input
################################################################################################################################################################################################################################################################################################################################################################################################

        #/!\ BEWARE pipes are handling the fabric of the digital reality. proceed carefully

        # get active window.
        if parent_connToAW.poll():
            active_window=parent_connToAW.recv()

            # if windows are displayed on current active workspace check if cursor is inside the window. [only if new data is received] ( a bit buggy but good enough )
            try:
                # i don't even know anymore, it works tho.
                hyprctl_clients_request = popen('hyprctl activewindow').read()
                active_window_pos = hyprctl_clients_request.partition("workspace:")[0].partition("at: ")[2].replace("\n","").replace(" ","").replace("size:", "a").replace(",","a")
                is_active_window_fullscreen = hyprctl_clients_request.partition('fullscreenClient:')[0]
                active_window_pos = "".join(c for c in active_window_pos if c.isalnum()).split("a")

            except ValueError:
                    pass
	# if no data return no pos
        if active_window_pos[0] == '':
                active_window_pos = [0,0,0,0]

        if (str(active_window).find('activewindow>>,') != -1 or isHovering_orClicking2D(Vector2(int(active_window_pos[0]), int(active_window_pos[1])), Vector2(int(active_window_pos[2]), int(active_window_pos[3])), cursor_pos, is_lmbClicking) == 0) and str(is_active_window_fullscreen).find('fullscreen: 2') == -1: # got no choice being here
            isWpFocused=True

        else:
            isWpFocused=False

        # check if should run
        if isWpFocused or isRunningWhenNotFocused:

            if parent_connToLMB.poll():
                mouse_clicks=parent_connToLMB.recv()

            if mouse_clicks!=" ": #to make sure data is relevant (int)
                last_press=int(mouse_clicks)
                if int(mouse_clicks)%2==0 and int(mouse_clicks)!=unload_lmb:

                    if tick< cancel_click_timer and tick > throttle_clickAmountFor:
                        unload_lmb=int(mouse_clicks)
                        is_lmbClicking = True

                        throttle_clickAmountFor = tick+2 # for some reason sometimes clicks happens 2 times in a row so i throttle
                        isDragging = False
                        print('has clicked at ',tick)

                    else:
                        cancel_click_timer=99999999
                        print('has clicked but was canceled at', tick)
                        throttle_clickAmountFor = tick+2 # for some reason sometimes clicks happens 2 times in a row
                        is_lmbClicking = False

                elif int(mouse_clicks)%2!=0:
                    isDragging = True

                    is_lmbClicking = False

                    cancel_click_timer = tick + win.framerate/4
                    print(cancel_click_timer)

                else:
                    is_lmbClicking=False
                    isDragging= False

            else:
                is_lmbClicking=False

                if last_press%2==0:
                    isDragging = False



            # get cursor pos
            if parent_connToCursorPos.poll():
                _cursor_pos= parent_connToCursorPos.recv().replace(",","").split()
                cursor_pos= Vector2(int(_cursor_pos[0]),int(_cursor_pos[1]))


        tick += 1
        dt = get_frame_time() # deltaTime

# draw scenes, beware referencing assets in the main loop will spawn them infinitely, don't forget to add flags
############################################################################################################################################################################################################################################################################################################################################


        scene_loader.scene1_update(camera, cursor_pos, is_lmbClicking, isDragging, tick, dt,cooldown_aw, isWpFocused, child_connToOS)

# you made it through
