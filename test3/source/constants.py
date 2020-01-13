'''保存游戏的基本设置，字符串信息'''

# 游戏的标题
ORIGINAL_CAPTION = 'Turn Base Strategy Game'  

GRID_X_LEN = 10 # 地图的行数
GRID_Y_LEN = 12 # 地图的列数
REC_SIZE = 50   # 地图每个格子的长度
MAP_WIDTH = GRID_X_LEN * REC_SIZE  # 地图的宽度
MAP_HEIGHT = GRID_Y_LEN * REC_SIZE # 地图的高度

SCREEN_WIDTH = MAP_WIDTH   # 游戏界面的宽度
SCREEN_HEIGHT = MAP_HEIGHT # 游戏界面的高度
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 游戏中使用到的颜色
#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
SKY_BLUE     = ( 39, 145, 251)
NAVYBLUE     = ( 60,  60, 100)
LIGHTYELLOW  = (247, 238, 214)

# 地图背景颜色类型
BG_EMPTY = 0
BG_ACTIVE = 1
BG_RANGE = 2

# 地图格子类型
MAP_EMPTY = 0 # 格子是空的
MAP_STONE = 1 # 格子中是石头
MAP_GRASS = 2 # 格子中是草地

# 地图配置文件中的属性
MAP_GRID = 'mapgrid'

# 开始关卡值
START_LEVEL_NUM = 1
# 最大关卡值
MAX_LEVEL_NUM = 2

# 游戏的状态类型
MAIN_MENU = 'main menu'
LEVEL_START = 'level start'
LEVEL_LOSE = 'level lose'
LEVEL_WIN = 'level win'
LEVEL = 'level'
EXIT = 'exit'

# 关卡失败信息
LEVEL_LOSE_INFO = 'You Lose'
# 关卡胜利信息
LEVEL_WIN_INFO = 'You Win'

# 状态间传递的信息
# 当前关卡值
LEVEL_NUM = 'level num'
