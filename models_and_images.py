#!/usr/bin/env python3
from pyray import *
from raylib import *
from nehj_wallpaper_custom_library import *
from window_utils import *
from math import fabs

class Soul:
    def __init__(self): # put where u want to init loads
        self.animsCount = ffi_int(1) # put the number of animation the model has here
        self.animIndex = 0
        self.anim_update_frame = 0
        self.load_model()
        self.load_animation()
        self.goUp = 1
        self.goDown = 1

    def load_model(self):
        self.model = load_model('./graphical_asset/soul.glb')
        self.pos = Vector3(0,-1,0)

    def load_animation(self):
        self.animationLoad = load_model_animations('./graphical_asset/soul.glb', self.animsCount)
        self.animation = self.animationLoad[0]
#-----------------------------------------------------------------------------------------------------------------------
    def update(self,ray=Ray(), tick=int): # put where is update
        self.tick = tick
        self.bounding_box(ray)
        self.update_animation()
        self.levitate_anim()


    def bounding_box(self, ray=Ray()):
        self.bb = get_bounding_box(self.model,self.pos)
        self.bbInf = GetRayCollisionBox(ray,self.bb)

    def update_animation(self):
        self.desired_anim_frameRate = self.animation.frameCount/60
        self.anim_update_frame = (int(self.anim_update_frame+self.desired_anim_frameRate))%self.animation.frameCount

    def levitate_anim(self):
        # determine the movement
        if self.tick%200 == 0 :
            if self.tick%(400) ==0:
                self.goUp = 1
                self.goDown = 1
               # print('debug1')
            else:
                self.goUp = -1
                self.goDown = -1

        self.pos.y +=  (self.goUp/1600)
    def unload(self):
        pass


## ---------------------------------------------------------------------------------------------------------------------
class RayWall:
    def __init__(self):
        self.model = load_model('./graphical_asset/plane_cube.glb')
        self.pos = Vector3(.0,.0,0)
        self.bb = get_bounding_box(self.model,self.pos)

    def update(self,ray=Ray()):
        self.bbInf = GetRayCollisionBox(ray,self.bb)


## -------------------------------------------------------------------------------------------------------------------
#to put in ui but i will prolly just delete anyway
class IconFirefox:
    def __init__(self):
        self.img = load_texture_from_image(load_image('/home/nehj/Pictures/firefox.png'))
        self.size = Vector2(128,128)
        self.pos = center_Rectangle(Vector2( 1920/2 , 1080/2 ), self.size)

    def update(self, cursor_pos, is_lmbClicking):
        self.bbInf = isHovering_orClicking2D(self.pos, self.size,     cursor_pos, is_lmbClicking)

