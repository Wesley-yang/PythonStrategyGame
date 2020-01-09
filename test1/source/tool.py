__author__ = 'marble_xu'

import os  #加载os模块
import json #加载json模块
import pygame as pg  #为了书写方便，将pygame缩写为pg
from . import constants as c #为了书写方便，将constants缩写为c
from . import level

class Control():
    def __init__(self):
        #screen会被pygame用来绘制图像
        self.screen = pg.display.get_surface()
        #done用来判断主循环是否要退出，done为True，游戏结束
        self.done = False 
        self.clock = pg.time.Clock()
        #fps 60表示pygame每秒钟会执行60次
        self.fps = 60
        #level是游戏运行类
        self.level = level.Level()
        self.mouse_pos = None #保存鼠标点击时的坐标

    def update(self):
        '''游戏的更新函数'''
        self.current_time = pg.time.get_ticks()
        self.level.update(self.screen, self.current_time, self.mouse_pos)
        self.mouse_pos = None

    def event_loop(self):
        '''获取pygame监听到的所有事件，这里我们只关心退出按钮和鼠标点击事件'''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                #当有点击退出按钮事件时，游戏退出
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                #当有鼠标点击事件时，保存鼠标的坐标
                self.mouse_pos = pg.mouse.get_pos()

    def main(self):
        while not self.done:
            #获取事件
            self.event_loop()
            #更新游戏状态
            self.update()
            #显示图像
            pg.display.update()
            #等待 1/self.fps 秒时间
            self.clock.tick(self.fps)
        print('game over')

def get_image(sheet, x, y, width, height, colorkey, scale):
    '''因为有的大图片里包含了很多小图片，所以要根据传入的坐标参数（x, y, width, height)
       指定小图片在大图片中的位置，将小图片截取出来，还可以根据参数scale将图片进行放大或缩小。'''
    image = pg.Surface([width, height])
    rect = image.get_rect()

    image.blit(sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pg.transform.scale(image, (int(rect.width*scale), int(rect.height*scale)))
    return image

def load_all_gfx(directory, colorkey=c.WHITE, accept=('.png', '.jpg', '.bmp', '.gif')):
    '''遍历传入参数表示的目录，将所有文件后缀名在accept tuple中的图片都加载到graphics字典中'''
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics

def load_map_grid_image():
    '''获取地图格子类型的图片'''
    grid_images = {}
    image_rect_dict = {c.MAP_STONE:(0, 16, 16, 16), c.MAP_GRASS:(0, 0, 16, 16)}
    for type, rect in image_rect_dict.items():
        grid_images[type] = get_image(GFX['tile'], *rect, c.WHITE, 3)
    return grid_images


pg.init() #pygame的初始化
pg.display.set_caption(c.ORIGINAL_CAPTION) #设置游戏窗口的标题
pg.display.set_mode(c.SCREEN_SIZE) #设置游戏窗口的大小（长度和宽度）

GFX = load_all_gfx(os.path.join("resources","graphics"))
GRID = load_map_grid_image()