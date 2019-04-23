#!/usr/bin/env python
# encoding: utf-8
'''
@author: shuiyuan.zhang
@license: (C) Copyright 2013-2019,
@contact: 742456376@qq.com
@software: garner
@file: TEST.py
@time: 2019/2/25 15:36
@desc:
'''
from concurrent.futures import ProcessPoolExecutor
import time, random, os

def task(name):
    print('%s %s is running' % (name, os.getpid()))
    time.sleep(random.randint(1, 3))

# if __name__ == '__main__':
#     p = ProcessPoolExecutor(4)  # 设置进程池内进程数
#     for i in range(10):
#         # 同步调用方式，调用和等值。
#         obj = p.submit(task, '进程pid：')  # 传参方式 （任务名，参数），参数使用位置参数或者关键字参数
#     res = obj.result()
#     p.shutdown(wait=True)  # 关闭进程池的入口，等待池内任务运行结束
#     print('主')