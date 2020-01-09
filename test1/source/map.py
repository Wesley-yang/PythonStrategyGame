import pygame as pg
from . import tool
from . import constants as c

class Map():
    def __init__(self, width, height, grid):
        self.width = width  #地图的行数
        self.height = height #地图的列数
        #bg_map是地图的背景颜色二维数组，每个元素对应一个地图格子。
        self.bg_map = [[0 for x in range(self.width)] for y in range(self.height)]
        self.setupMapImage(grid)

    def setupMapImage(self, grid):
        #grid_map是地图的格子类型二维数组，每个元素对应一个地图格子
        self.grid_map = [[0 for x in range(self.width)] for y in range(self.height)]
        if grid is not None:
            for data in grid:
                x, y, type = data['x'], data['y'], data['type']
                self.grid_map[y][x] = type
        
        #创建一个和地图一样大小的图片map_image，用来绘制非空的地图格子，比如格子是石块或草地。
        self.map_image = pg.Surface((self.width * c.REC_SIZE, self.height * c.REC_SIZE)).convert()
        self.rect = self.map_image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        for y in range(self.height):
            for x in range(self.width):
                type = self.grid_map[y][x]
                if type != c.MAP_EMPTY:
                    self.map_image.blit(tool.GRID[type], (x * c.REC_SIZE, y * c.REC_SIZE))
        self.map_image.set_colorkey(c.BLACK)

    def isValid(self, map_x, map_y):
        '''判断传入的地图x和y的值是否是有效的'''
        if (map_x < 0 or map_x >= self.width or
            map_y < 0 or map_y >= self.height):
            return False
        return True

    def getMapIndex(self, x, y):
        '''根据传入的坐标x和y值，返回坐标所在的格子位置'''
        return (x//c.REC_SIZE, y//c.REC_SIZE)

    def setMouseClick(self, mouse_pos):
        '''设置鼠标点击的背景格子类型为c.BG_ACTIVE，'''
        x, y = mouse_pos
        map_x, map_y = self.getMapIndex(x, y)
        for y in range(self.height):
            for x in range(self.width):
                self.bg_map[y][x] = c.BG_EMPTY

        if self.isValid(map_x, map_y):
            self.bg_map[map_y][map_x] = c.BG_ACTIVE

    def drawBackground(self, surface):
        #根据背景格子类型，设置地图格子为不同的颜色
        for y in range(self.height):
            for x in range(self.width):
                if self.bg_map[y][x] == c.BG_EMPTY:
                    color = c.LIGHTYELLOW
                elif self.bg_map[y][x] == c.BG_ACTIVE:
                    color = c.SKY_BLUE
                pg.draw.rect(surface, color, (x * c.REC_SIZE, y * c.REC_SIZE, 
                        c.REC_SIZE, c.REC_SIZE))
        
        #绘制格子类型的图片
        surface.blit(self.map_image, self.rect)

        #绘制地图每一行的线
        for y in range(self.height):
            # draw a horizontal line
            start_pos = (0, 0 + c.REC_SIZE * y)
            end_pos = (c.MAP_WIDTH, c.REC_SIZE * y)
            pg.draw.line(surface, c.BLACK, start_pos, end_pos, 1)
        
        #绘制地图每一列的线
        for x in range(self.width):
            # draw a vertical line
            start_pos = (c.REC_SIZE * x, 0) 
            end_pos = (c.REC_SIZE * x, c.MAP_HEIGHT)
            pg.draw.line(surface, c.BLACK, start_pos, end_pos, 1)
