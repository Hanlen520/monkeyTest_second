#!/usr/bin/env python
# encoding: utf-8
'''
@author: shuiyuan.zhang
@license: (C) Copyright 2013-2019,
@contact: 742456376@qq.com
@time: 2019/3/21 13:41
@desc:
'''



import os
import subprocess
import time

#判断是否存在monkey日志，若存在，删除手机里的monkey日志
def deleteMonkeylog(dev):
    crash_log_cmd = "adb -s "+dev+" shell ls sdcard|findstr crash-dump.log"
    # oom_log_cmd = "adb -s "+dev+" shell ls sdcard|findstr oom-traces.log"
    crash_log = subprocess.Popen(crash_log_cmd, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE).stdout.readlines()
    print(crash_log)
    # oom_log = subprocess.Popen(oom_log_cmd, shell=True, stdout=subprocess.PIPE,
    #                            stderr=subprocess.PIPE).stdout.readlines().split()
    # if crash_log !=[]:
    #     delcrash_cmd = "adb -s "+dev+" shell rm /sdcard/crash-dump.log"
    #     delcrash_file = subprocess.Popen(delcrash_cmd, shell=True, stdout=subprocess.PIPE,
    #                                      stderr=subprocess.PIPE).stdout.readlines().split()
    # else:
    #     print(" No this File :crash-dump.log ")



def pushmonkey(dev):
    monkey_jar=os.popen("adb -s " +dev +"  shell ls sdcard|findstr monkey.jar").read().split()
    framework_jar=os.popen("adb  -s " +dev +"  shell ls sdcard|findstr framework.jar").read().split()
    name1='monkey.jar'
    name2='framework.jar'
    path1=os.path.abspath(name1)
    path2=os.path.abspath(name2)
    if monkey_jar ==[] and framework_jar ==[]:
        cmd1="adb -s "+dev+"  push  "+path1+"  /sdcard"
        cmd2="adb -s "+dev+"  push  "+path2+"  /sdcard"
        push_monkey=subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        push_framework=subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        time.sleep(2)
        print ("monkey.jar导入"+dev+"成功")
        print ("framework.jar导入"+dev+"成功")
    elif monkey_jar !=[] and framework_jar ==[]:
        cmd2="adb -s "+dev+" push "+path2+" /sdcard"
        push_framework=subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        time.sleep(2)
        print ("framework.jar导入"+dev+"成功")
    elif monkey_jar == [] and framework_jar !=[]:
        cmd1="adb -s "+dev+" push "+path1+" /sdcard"
        push_monkey=subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        time.sleep(2)
        print ("monkey.jar导入"+dev+"成功")
    else:
        print ("当前设备："+dev+"中存在monkey.jar和framework.jar")

if __name__ == '__main__':
    deleteMonkeylog("55Z5NZSOLZY9S4NF")
