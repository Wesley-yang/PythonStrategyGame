import pygame as pg
from source import tool

def main():
    # 创建游戏的控制类
    game = tool.Control()
    # 游戏的主循环
    game.main()

if __name__=='__main__':
    # 游戏的执行入口
    main()
    # 释放pygame的资源
    pg.quit()
