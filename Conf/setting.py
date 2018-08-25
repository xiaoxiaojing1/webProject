"""
Created by xiaoxiaojing on 2018/8/25
"""
import unittest
import time
import datetime
from selenium import webdriver

import os
import sys

current_path = os.path.abspath(os.path.dirname("__file__"))  # 当前目录
project_path = os.path.split(current_path)[0]  # 项目目录
top_path = os.path.split(project_path)[0]  # 项目所在目录
test_path = project_path + "/test_case"
print("当前目录为：", current_path)
print("项目目录为：", project_path)
print("项目所在目录为：", top_path)
print("测试用例路径为：", test_path)

sys.path.append(top_path)  # 为python的搜索模块list添加value
print(sys.path)

Debug = False


