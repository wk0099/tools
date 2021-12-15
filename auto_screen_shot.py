#! /usr/bin/env python
# coding=utf-8

# ==============================
# Describe:      后台自动定时截屏
# D&P Author:             常成功
# Environment:    Python 2.7.15
# Create Date:       2020/07/07
# ==============================

import time
import os
from PIL import ImageGrab

# 获取当前目录
BASE_DIR = os.getcwd()


# 截屏函数
def screenshot():
    local_tm = time.localtime(time.time())
    # 格式化日期: 年月日
    date_str = time.strftime("%Y%m%d", local_tm)
    # 以日期建立文件夹
    dir_name = "Screenshot_" + date_str
    dir_path = os.path.join(BASE_DIR, dir_name)
    # 不存在这一天的文件夹, 则建立它
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # 格式化时间: 年月日_时分秒
    YMD_HMS_str = time.strftime("%Y%m%d_%H%M%S", local_tm)
    # 文件保存为.jpg (也可以是png或者其他格式)
    file_name = YMD_HMS_str + ".jpg"
    file_path = os.path.join(dir_path, file_name)
    # 截屏, 抓取当前屏幕的快照，返回一个模式为"RGB"的图像
    im = ImageGrab.grab()
    im.save(file_path)
    # 输出已经保存的截图文件, 以及截图尺寸 (比如: 560, 1440)
    print("save: ", file_path, " size:", im.size)


# 基于 Python Imaging Library(PIL) 的截屏实现
if __name__ == '__main__':
    print("Now, Run Auto_Screenshot: ", BASE_DIR)

    while True:
        screenshot()
        # 每隔60秒运行一次截屏
        time.sleep(10)