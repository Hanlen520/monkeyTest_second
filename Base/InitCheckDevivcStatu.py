#!/usr/bin/env python
# encoding: utf-8
'''
@author: shuiyuan.zhang
@license: (C) Copyright 2013-2019,
@contact: 742456376@qq.com
@software: garner
@file: InitCheckDevivcStatu.py
@time: 2019/3/21 14:37
@desc:
'''

import os
import subprocess
from Base import AdbCommon


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

ADB = AdbCommon.AndroidDebugBridge()
osPlatform = ADB.osVersion()

#判断是否存在monkey日志，若存在，删除手机里的monkey日志
def InitCheckMonkeylog(devices):
    crash_log_cmd = "adb -s "+devices+" shell ls sdcard|"+osPlatform+" crash-dump.log"
    oom_log_cmd = "adb -s "+devices+" shell ls sdcard|"+osPlatform+" oom-traces.log"
    crash_log = subprocess.Popen(crash_log_cmd, shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE).stdout.readlines()
    oom_log = subprocess.Popen(oom_log_cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).stdout.readlines()
    if crash_log !=[] and oom_log!= []:
        delcrashLog_cmd = "adb -s "+ devices + " shell rm /sdcard/crash-dump.log"
        deloomLog_cmd = "adb -s "+ devices + " shell rm /sdcard/oom-traces.log"
        delcrashLog = subprocess.Popen(deloomLog_cmd,shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE).stdout.readlines()
        deloomLog = subprocess.Popen(delcrashLog_cmd,shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE).stdout.readlines()
        if delcrashLog ==[] and deloomLog == []:
            print("crashLog and oomLog have been del")
        elif delcrashLog !=[] and deloomLog == []:
            print("crashlog is no del,oomlog have been del")
        elif delcrashLog == [] and deloomLog !=[]:
            print("crashlog haver been del,oomlog is no del")
        else:
            print("crashlog and oomlog  is no del")
    else:
        print("Device:"+devices+" have no monkeylog")

#把当前目录下的文件(monkey.jar/firamework.jar)push进手机sdcard根目录
def InitMonkeyJar(dev):
    monkey_jarpath = ADB.file_path("jar")+"\\monkey.jar"
    framework_jarpath = ADB.file_path("jar")+"\\framework.jar"
    print(monkey_jarpath)
    print(framework_jarpath)
    monkey_jar=os.popen("adb -s " +dev +"  shell ls sdcard|"+osPlatform+" monkey.jar").read().split()
    framework_jar=os.popen("adb  -s " +dev +"  shell ls sdcard|"+osPlatform+" framework.jar").read().split()
    if monkey_jar ==[] and framework_jar ==[]:
        ADB.push(monkey_jarpath,"/sdcard")
        ADB.push(framework_jarpath,"/sdcard")
        print("monkey.jar and framework.jar have been push")
    elif monkey_jar !=[] and framework_jar ==[]:
        ADB.push(framework_jarpath,"/sdcard")
        print("framework.jar have been push")
    elif monkey_jar == [] and framework_jar !=[]:
        ADB.push(monkey_jarpath,"/sdcard")
        print("monkey.jar have been push")
    else:
        print ("device: "+dev+" have monkey.jar and framework.jar")


def InitApk_name():
    # 获取当前文件所在的路径即InstallApk所在路径
    APKpath =ADB.file_path("Apk")
    print(APKpath)
    for (thisdir,subsHere,filesHere) in os.walk(APKpath):
    #thisdir:该目录下的所有的文件夹  subsHere:当前目录下所有的子目录 filesHere:当前目录下所有的文件
    #用walk函数打印目录树
        for apkname in filesHere + subsHere:
            if apkname[len(apkname) - 3:len(apkname)] == "apk":
                #增加判断应用名称是否有空格
                if " " in apkname:
                    new =apkname.replace(" ","_")
                    os.renames(apkname,new)
                    apkname = new
                    print("APK_name: "+apkname)
                else:
                    print("APK_name: "+apkname)
                found =[]
                apkname=apkname.lower()# lower()方法转换字符串中所有大写字符为小写。
                if apkname in apkname.lower():
                    found.append(os.path.join(thisdir,apkname))
                #print(found)
                if found == []:
                    print("No apk")
                else:
                    print("APK : "+found[0])
                    apkPath=found[0]

# #批量安装APK
# def install_apk(dev):
#     ADB.Apkinstall_detail()

    # # 获取当前文件所在的路径即InstallApk所在路径
    # APKpath =ADB.file_path("Apk")
    # print(APKpath)
    # for (thisdir,subsHere,filesHere) in os.walk(APKpath):
    #     #thisdir:该目录下的所有的文件夹  subsHere:当前目录下所有的子目录 filesHere:当前目录下所有的文件
    #     #用walk函数打印目录树
    #     print(subsHere)
    #     print(filesHere)





if __name__ == '__main__':
    InitMonkeyJar("04078258C5100082")
    # InitApk_name()


