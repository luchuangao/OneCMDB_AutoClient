import os
os.environ['USER_SETTINGS'] = "config.settings"
import sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from src import script
if __name__ == '__main__':
    script.run()

    # from src.plugins import PluginManager
    # 没有参数，默认使用agent方式进行连接, 相对得应该配置settings中的MODE为AGENT
    # server_info = PluginManager().exec_plugin()

    # 有参数得情况下，需要判断settings中的MODE是为SSH或SALT
    # server_info = PluginManager('c1.com').exec_plugin()

    # server_info = PluginManager().exec_plugin()
    # """
    #     {
    #          "cpu": {'status':True,'data': xxxxx},
    #          "cpu": {'status':True,'data': xxxxx},
    #          "cpu": {'status':True,'data': xxxxx},
    #     }
    # """
    # for k,v in server_info.items():
    #     print(k,v)