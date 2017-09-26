# OneCMDB
基于Django实现CMDB

##### 目录规范
* bin 	可执行文件
* config 	配置文件
* lib 	公共模块
* src 	业务逻辑
* log【由于日志占用空间太大，不易放在程序目录】

##### 配置文件
配置文件分为默认配置文件和自定义配置文件，自定义配置文件优先于默认配置文
知识点：
1. 字符串导入模块
2. 反射

Django中默认的配置文件：  
from django.conf import global_settings

用户自定义配置文件：settings.py  
默认配置文件：global_settings.py  















