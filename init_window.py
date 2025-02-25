#!/usr/bin/env python3

from raylib import *
from pyray import *
from time import *


class Window:
    def __init__(self,widht=1920,height=1080,name="x-bg",framerate=24):
        self.widht = widht
        self.height = height
        self.framerate = framerate
        self.name = name

    def load_window(self):
        init_window(self.widht,self.height,self.name)
        set_target_fps(self.framerate)
        sleep(.3)



class CameraObj:
    def __init__(self,pos = Vector3(0.0, .0,4.),projection=CAMERA_ORTHOGRAPHIC,fovy=45, target = Vector3(0,0,0), upvec = Vector3(0,1,0),camera=[]):
        self.camera = camera
        self.pos = pos
        self.target = target
        self.upvec = upvec
        self.fovy = fovy
        self.projection = projection
        self.default_cam_pos = self.pos


    def init_camera(self): # can update values
        self.camera = Camera3D()
        self.camera.position = self.pos
        self.camera.target = self.target
        self.camera.up = self.upvec
        self.camera.fovy = self.fovy

        self.camera2 = Camera3D()
        self.camera2.position = Vector3(self.pos.x,self.pos.y-.1,self.pos.z)
        self.camera2.target = self.target
        self.camera2.up = self.upvec
        self.camera2.fovy = self.fovy
