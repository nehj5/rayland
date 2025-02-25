#!/usr/bin/env python3

from pyray import *; from raylib import *; from window_utils import *

class UI3D_hud:
    def __init__(self):
        pass

    def bg_soul(self):
        self.model = load_model('./graphical_asset/ui_soul_bg2.glb')
        self.pos = Vector3(-3,0,-1)


class UI:
    def __init__(self):
        pass

    def background_init(self):
        self.img = load_texture_from_image(load_image('./graphical_asset/ui_bg.png'))
        self.pos = Vector2(0,0)


class UI3D_buttons:
    def __init__(self):
        self.model = load_model('./graphical_asset/ui_button.glb')
        self.distance_main = -.55
        self.web_init()
        self.kitty_init()
        self.diary_init()
    
    def web_init(self):
        self.web_pos = Vector3(-1.1, .55, .0)

    def web_update(self):
        self.web_bb = get_bounding_box(self.model,self.web_pos)
        self.web_bbInf = GetRayCollisionBox(self.ray,self.web_bb)

    def kitty_init(self):
        self.kitty_pos = Vector3(self.web_pos.x, self.web_pos.y+ self.distance_main, 0)
        

    def kitty_update(self):
        self.kitty_bb = get_bounding_box(self.model,self.kitty_pos)
        self.kitty_bbInf = GetRayCollisionBox(self.ray,self.kitty_bb)

        if self.kitty_bbInf.hit and self.is_lmbClicking and self.isWpFocused:
            if self.tick > self.cooldown_aw:
                self.cooldown_aw = self.tick+10
                self.child_connToOS.send("kitty")
                
    def diary_init(self):
        self.diary_pos = Vector3(self.web_pos.x, self.web_pos.y+ self.distance_main*2, 0)
        
        
    def diary_update(self):
        self.diary_bb = get_bounding_box(self.model,self.diary_pos)
        self.diary_bbInf = GetRayCollisionBox(self.ray,self.diary_bb)


    def update(self,ray, is_lmbClicking,tick,cooldown_aw,isWpFocused, child_connToOS):
        self.child_connToOS = child_connToOS; self.ray = ray; self.is_lmbClicking = is_lmbClicking; self.tick = tick; self.cooldown_aw = cooldown_aw; self.isWpFocused = isWpFocused
        self.web_update()
        self.kitty_update()
        self.diary_update()

        

    
