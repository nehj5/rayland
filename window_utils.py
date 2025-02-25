#!/usr/bin/env python3

from pyray import *
from raylib import *
from math import cos, sin




# drags

def dragModel(bbinf,tbbinf,pos,isDragging,offset_x=0.0,offset_y=0.0):
    if bbinf.hit and isDragging:
        pos.x = tbbinf.point.x+offset_x; pos.y = tbbinf.point.y+offset_y


def center_Rectangle(pos=Vector2,size=Vector2):
    center = Vector2(pos.x - size.x/2 ,pos.y - size.y/2)
    return center


def dragRectangle(pos_rect=Vector2, size=Vector2,bbinf2D_hit=any,cursor_pos=any,isDragging=bool):
    if bbinf2D_hit>0 and isDragging:
        pos_rect.x = center_Rectangle(cursor_pos,size).x; pos_rect.y = center_Rectangle(cursor_pos,size).y


# bounding box & collision

def get_bounding_box(model,pos):
    bounding_box= get_mesh_bounding_box(model.meshes[0])
    min_boundary= Vector3Add(pos,bounding_box.min)
    max_boundary= Vector3Add(pos,bounding_box.max)
    return BoundingBox(min_boundary,max_boundary)


def isHovering_orClicking2D(tl_pos=Vector2, size=Vector2, cursor_pos=Vector2, is_lmbClicking=any) : # return not hovering, hovering or clicking
   
    p= [cursor_pos.x, cursor_pos.y]
    bl=[tl_pos.x, tl_pos.y+size.y]
    tr=[tl_pos.x+size.x, tl_pos.y]

    if (int(p[0]) > bl[0] and int(p[0]) < tr[0] and int(p[1]) < bl[1] and int(p[1]) > tr[1]):
    
        if is_lmbClicking == True:
            return 2
        else:
            return 1
        
    else:
        return 0
    


# textures 
def set_objects_texture_alpha_zero(model):
    set_material_texture(model.materials[2],MATERIAL_MAP_ALBEDO,RED)

# a nice gradient
#cube_gradient = load_texture_from_image(gen_image_gradient_linear(10,10,1,RED,YELLOW))


# rotation

def rotate_cam_around_o(self,camera,rotCamSpeed,tick,dt):
    camera.position.x = ((self.default_cam_pos.x)*cos(dt*tick*rotCamSpeed))-((self.default_cam_pos.z)*sin(dt*tick*rotCamSpeed))
    camera.position.z = ((self.default_cam_pos.z)*cos(dt*tick*rotCamSpeed))+((self.default_cam_pos.x)*sin(dt*tick*rotCamSpeed))


def rotate(model,speed,axis,deltaTime): #rotate object
   
    if axis=='x':
        model.transform = MatrixMultiply(MatrixRotateX(speed*deltaTime), model.transform)
    elif axis=='z':
        model.transform = MatrixMultiply(MatrixRotateZ(speed*deltaTime), model.transform)
    elif axis=='y':
        model.transform = MatrixMultiply(MatrixRotateY(speed*deltaTime), model.transform)

    else:
        print('axis not found, please specify x,y or z')
