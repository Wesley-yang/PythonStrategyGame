import pygame as pg
from . import tool
from . import constants as c
from . import aStarSearch
from . import map


class Entity():
    def __init__(self, group, name, map_x, map_y):
        self.group = group
        self.group_id = group.group_id
        self.map_x = map_x
        self.map_y = map_y
        self.frames = []
        self.frame_index = 0
        self.loadFrames(name)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.getRectPos(map_x, map_y)

        self.state = c.IDLE
        self.animate_timer = 0.0
        self.current_time = 0.0
        self.move_speed = c.MOVE_SPEED
        self.distance = 4
    
    def getMapIndex(self):
        return (self.map_x, self.map_y)

    def getRectPos(self, map_x, map_y):
        return(map_x * c.REC_SIZE + 5, map_y * c.REC_SIZE + 8)

    def getRecIndex(self, x, y):
        return (x // c.REC_SIZE, y // c.REC_SIZE)

    def loadFrames(self, name):
        frame_rect_list = [(64, 0, 32, 32), (96, 0, 32, 32)]
        for frame_rect in frame_rect_list:
            self.frames.append(tool.getImage(tool.GFX[name], 
                    *frame_rect, c.BLACK, c.SIZE_MULTIPLIER))
        
    def setDestination(self, map_x, map_y):
        self.dest_x, self.dest_y = self.getRectPos(map_x, map_y)
        self.next_x, self.next_y = self.rect.x, self.rect.y
        self.state = c.WALK

    def walkToDestination(self, map):
        if self.rect.x == self.next_x and self.rect.y == self.next_y:
            source = self.getRecIndex(self.rect.x, self.rect.y)
            dest = self.getRecIndex(self.dest_x, self.dest_y)
            location = aStarSearch.AStarSearch(map, source, dest)
            if location is not None:
                map_x, map_y, _ = aStarSearch.getFirstStepAndDistance(location)
                self.next_x, self.next_y = self.getRectPos(map_x, map_y)
            else:
                self.state = c.IDLE

        if self.rect.x != self.next_x:
            self.rect.x += self.move_speed if self.rect.x < self.next_x else -self.move_speed
        elif self.rect.y != self.next_y:
            self.rect.y += self.move_speed if self.rect.y < self.next_y else -self.move_speed

    def update(self, current_time, map):
        self.current_time = current_time
        if self.state == c.WALK:
            if (self.current_time - self.animate_timer) > 250:
                if self.frame_index == 0:
                    self.frame_index = 1
                else:
                    self.frame_index = 0
                self.animate_timer = self.current_time

            if self.rect.x != self.dest_x or self.rect.y != self.dest_y:
                self.walkToDestination(map)
            else:
                map.setEntity(self.map_x, self.map_y, None)
                self.map_x, self.map_y = self.getRecIndex(self.dest_x, self.dest_y)
                map.setEntity(self.map_x, self.map_y, self)
                self.state = c.IDLE
        
        if self.state == c.IDLE:
            self.frame_index = 0

    def draw(self, surface):
        self.image = self.frames[self.frame_index]
        surface.blit(self.image, self.rect)


class EntityGroup():
    def __init__(self, group_id):
        self.group = []
        self.group_id = group_id
        self.entity_index = 0

    def createEntity(self, entity_list, map):
        for data in entity_list:
            entity_name, map_x, map_y = data['name'], data['x'], data['y']
            if map_x < 0:
                map_x = c.GRID_X_LEN + map_x
            if map_y < 0:
                map_y = c.GRID_Y_LEN + map_y
            
            entity = Entity(self, entity_name, map_x, map_y)
            self.group.append(entity)
            map.setEntity(map_x, map_y, entity)
        #self.group = sorted(self.group, key=lambda x:x.attr.speed, reverse=True)

    def removeEntity(self, entity):
        for i in range(len(self.group)):
            if self.group[i] == entity:
                if (self.entity_index > i or
                    (self.entity_index >= len(self.group) - 1)):
                    self.entity_index -= 1
        self.group.remove(entity)

    def nextTurn(self):
        self.entity_index = 0

    def getActiveEntity(self):
        if self.entity_index >= len(self.group):
            entity = None
        else:
            entity = self.group[self.entity_index]
        return entity

    def consumeEntity(self):
        self.entity_index += 1

    def update(self, game_info, map):
        for entity in self.group:
            entity.update(game_info, map)

    def draw(self, surface):
        for entity in self.group:
            entity.draw(surface)