# OneCMDB_AutoClient
基于Django实现CMDB客户端

#### 目录规范
* bin 	可执行文件
* config 	配置文件
* lib 	公共模块
* lib/convert.py 类型转换，将MB转换成GB
* src 	业务逻辑
* src/client.py 向API获取数据发送数据文件
* src/script.py 调用src/client.py得文件
* src/plugins 自定义插件
* log【由于日志占用空间太大，不易放在程序目录】
* files   调试文件


#### 配置文件
配置文件分为默认配置文件和自定义配置文件，自定义配置文件优先于默认配置文
知识点：
1. 字符串导入模块
2. 反射

Django中默认的配置文件：  
from django.conf import global_settings

用户自定义配置文件：settings.py  
默认配置文件：global_settings.py  


#### 开发资产插件（可插拔）
每个公司采集得资产类型有差别，可以通过添加配置和自定义插件来实现，每个插件预留了钩子initial，可以自行扩展。  
插件遵循：高内聚、低耦合原理。

根据不同模式，执行不同的命令，可以使用两种方式来实现：
1. 定义基类 base.py，让所有的自定义插件类继承基类，在基类中进行判断MODE
2. 给src/plugins/__init__.py 中的PluginManager定义command方法，进行判断客户端选择得MODE 【推荐，比较简单】

插件运行模式：
1. DEBUG模式，DEBUG模式，在配置文件中把DEBUG=True
1. 非DEBUG模式，把DEBUG=False

知识点：  
1. 字符串导入模块
2. 反射
3. 错误堆栈信息 traceback

注意点： 
1. salt现在只支持py2，如果想再py3环境中执行salt，需要使用subprocess来执行 

默认资产类型：  
1. baisc
2. board
3. cpu
4. disk
5. memory
6. nic

定义插件：在src/plugins目录定义  

配置文件：在config/settings.py中

执行命令：需要额外安装
1. MegaCli  【磁盘命令】
2. dmidecode【内存命令】

#### 向API获取数据发送数据

文件路径：src/client.py  
执行文件：src/script.py

AGENT定时发送数据即可:向API发送资产信息  
SSH、SALT先通过API获取未采集的主机，然后进行获取未采集的主机信息，最后向API发送资产信息


#### 唯一标识

使用主机名作为唯一标识，依赖本地文件

唯一标识文件：config/cert

修改代码：src/client.py

#### 线程池

为提高SSH、SALT并发能力，引入线程池  
from concurrent.futures import ThreadPoolExecutor

注：ThreadPoolExecutor在py2不支持，只支持py3

修改代码：src/client.py







