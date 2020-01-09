import os
import json
import pygame as pg
from . import tool
from . import constants as c
from . import map

class Level():
    def __init__(self):
        self.loadMap()
        # 如果在地图配置文件中设置了格子信息，则读取出来
        grid = self.map_data[c.MAP_GRID] if c.MAP_GRID in self.map_data else None
        # 创建地图类
        self.map = map.Map(c.GRID_X_LEN, c.GRID_Y_LEN, grid)
    
    def loadMap(self):
        '''加载地图配置文件'''
        map_file = 'level_1.json'
        file_path = os.path.join('data', 'map', map_file)
        f = open(file_path)
        # json.load 函数将json文件内容解析后返回一个字典
        self.map_data = json.load(f)
        f.close()

    def update(self, surface, current_time, mouse_pos):
        '''游戏的更新函数'''
        self.current_time = current_time
        if mouse_pos is not None:
            # mouse_pos 不是None，表示有鼠标点击事件
            self.mouseClick(mouse_pos)
        self.draw(surface)

    def mouseClick(self, mouse_pos):
        '''有鼠标点击时，修改鼠标所在的地图格子颜色'''
        self.map.setMouseClick(mouse_pos)
        
    def draw(self, surface):
        '''绘制游戏运行时的界面'''
        self.map.drawBackground(surface)
        
