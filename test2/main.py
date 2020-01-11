import pygame as pg
from source import constants as c
from source import tool, screen, level

def main():
    # 创建游戏的控制类
    game = tool.Control()
    # 创建游戏的状态类字典
    state_dict = {c.MAIN_MENU: screen.MainMenu(),
                  c.LEVEL_START: screen.LevelStartScreen(),
                  c.LEVEL_LOSE: screen.LevelLoseScreen(),
                  c.LEVEL_WIN: screen.LevelWinScreen(),
                  c.LEVEL: level.Level()}
    # 加状态类字典加入到控制类中，并设置游戏的启动状态
    game.setup_states(state_dict, c.MAIN_MENU)
    # 游戏的主循环
    game.main()

if __name__=='__main__':
    # 游戏的执行入口
    main()
    # 释放pygame的资源
    pg.quit()
