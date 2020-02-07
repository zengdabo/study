#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

cha_path = input("输入查找路径:")

# 考虑到输入路径可能会出现'c:\aaa'和'c:\aaa\'【linux下'/aaa'和'/aaa/'】两种写法。下面加了一个if语句

cha_file = input("输入查找的字符串:")

for dir in os.walk(cha_path):
    for x in dir[-1]:

        if x.find(cha_file) != -1:
            y = os.path.join(dir[0], x)
            if cha_path[-1] == "/" or cha_path[-1] == "\\":
                z = y.replace(cha_path[:-1], ".")
            else:
                z = y.replace(cha_path, ".")
            # print("文件名为：%s\n绝对路径为：%s\n对比输入目录的相对路径为：%s\n\n\n" % (x, y, z))
            print(z)

