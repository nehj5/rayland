#!/usr/bin/env python3


from pyray import *
from raylib import *
from nehj_wallpaper_custom_library import *
from models_and_images import *
from window_utils import *
from ui import *




# referencing assets
############################################################################################################################################################################################################################################################################

class SceneLoader:
    def __init__(self):
        #debugging ?
        self.debug=True
        self.isScene1 = True
        self.init_scene1()


#    def get_vars(self,is_lmbClicking,cursor_pos,isDragging,initDraggingTimer,isinitDragging,ray,tick,dt):
 #       self.is_lmbClicking = is_lmbClicking; self.cursor_pos = cursor_pos; self.isDragging = isDragging; self.initDraggingTimer = initDraggingTimer; self.isinitDragging = isinitDragging; self.ray = ray; self.tick = tick; self.dt = dt


    def init_scene1(self):
        if self.isScene1 == True:

            # loading assets

            # 3d
            self.raywall = RayWall()
            self.soul = Soul()

            #2d
            self.firefox = IconFirefox()

            #ui
            self.ui_bg_soul = UI3D_hud()
            self.ui_bg_soul.bg_soul()
            self.bg = UI()
            self.bg.background_init()
            self.m_buttons = UI3D_buttons()

            #font
            self.source_code_pro = load_font('/usr/share/fonts/adobe-source-code-pro-fonts/SourceCodePro-Medium.otf')

#--------------------------------------------------------------------------------------------------------------------------------------------------------

    def scene1_update(self,cam,cursor_pos=Vector2, isLmb_clicking=bool, isDragging=bool,tick=int, dt=float,cooldown_aw=any,isWpFocused=any, child_connToOS=any):

        if self.isScene1 == True:

            self.ray = GetScreenToWorldRay(cursor_pos, cam.camera2) # camera 2 is slighty offset down

            # updating assets
            self.raywall.update(self.ray)
            self.soul.update(self.ray, tick)
            self.firefox.update(cursor_pos,isLmb_clicking)
            # updating ui
          #  self.m_buttons.update(self.ray, isLmb_clicking,tick,cooldown_aw, isWpFocused, child_connToOS)

            # managing drags
            dragModel(self.soul.bbInf,self.raywall.bbInf, self.soul.pos,isDragging, 0, 0)
            dragRectangle(self.firefox.pos, self.firefox.size, self.firefox.bbInf, cursor_pos, isDragging)

            # update animations
            update_model_animation(self.soul.model, self.soul.animation , self.soul.anim_update_frame)
           # rotate(self.soul.model,1.0,'y',dt)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            # begin render
            begin_drawing()
            clear_background(BLUE)

            # 2d that goes under 3d
            if "2d" == "2d":
                draw_texture_ex(self.bg.img, self.bg.pos,0,1, WHITE)

            # begin 3d mod
            begin_mode_3d(cam.camera)

            if "3d" == "3d":
                # 3d models
                draw_model(self.soul.model, self.soul.pos, 1, WHITE)


                # ui
                #draw_model(self.ui_bg_soul.model, self.ui_bg_soul.pos, 1, BLACK)
                #draw_model(self.m_buttons.model, self.m_buttons.web_pos, 1, BLUE)
                #draw_model(self.m_buttons.model, self.m_buttons.kitty_pos, 1, BLUE)
                #draw_model(self.m_buttons.model, self.m_buttons.diary_pos, 1, BLUE)

                if self.debug == False:
                    draw_bounding_box(self.soul.bb,RED)
                    DrawRay(self.ray,RED)

            end_mode_3d()

            # 2d that goes over 3d
            if "2d" == "2d":
                #draw_texture_ex(self.firefox.img, self.firefox.pos,0,1,WHITE)
                draw_text("2d.x =" + str(cursor_pos.x) + " | 2d.y =" + str(cursor_pos.y),int(1450)+100,int(850)+30,20, GREEN)
                draw_text("3d.x =" + str("%.2f" %self.raywall.bbInf.point.x) + " | 3d.y =" + str("%.2f" %self.raywall.bbInf.point.y),int(1450)+100,int(900)+30,20, GREEN)
                draw_text_ex(self.source_code_pro, "n.os - v0.0.4a", Vector2(860,42), 30, 0, BLACK )


            end_drawing()


    def close():
        unload_texture()
        close_window()



































