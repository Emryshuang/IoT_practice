# IoT_practice
一个小型物联网简易系统 arduino+raspberry+One net 
# 环境配置
## 树莓派python环境配置

1. 创建和激活 VirtualEnvironments

2. 使用pip自动安装linkkit

`pip install aliyun-iot-linkkit`

3. 使用pip自动安装Advanced Python Scheduler（APScheduler）

`pip install apscheduler`

## arduino 设备配置
1. arduino需要准备：
    1. Arduino Uno
    2. DHT11 温湿度传感器
    3. 130 DC Motor 电机
    4. LED灯
2. led灯、温湿度传感器、电机通过宏定义确定pin脚位置，需要根据实际情况修改arduino/test/test.ino。
```c
#define DHTPIN 2     
#define DHTTYPE DHT11   
#define motorPin  10;   
```
3. 将 arduino/environment.ino烧录进arduino uno。

## 树莓派与arduino连接
根据串口地址，修改raspberryPi/ArduinoUSB.py中串口地址。

## One net云平台设置

1. 创建新的产品
2. 创建相应的设备
3. 创建与设备数据相应的应用
4. 修改raspberryPi/main.py中的设备id，key码等信息。