"""
用户自定义配置文件
"""

import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER = "root"
PWD = "123.com"

# debug模式
DEBUG = True

MODE = "AGENT" # SALT, SSH
SSH_USER = "root"
SSH_PWD = "root"
SSH_KEY = "/xxx/xxx/xx"
SSH_PORT = 22

# 插件配置文件
PLUGINS_DICT = {
    'basic': "src.plugins.basic.Basic",
    'board': "src.plugins.board.Board",
    'cpu': "src.plugins.cpu.Cpu",
    'disk': "src.plugins.disk.Disk",
    'memory': "src.plugins.memory.Memory",
    'nic': "src.plugins.nic.Nic",
}



