# python module for interacting with adb
# -*- coding: utf-8 -*-

import subprocess

__author__ = 'shuiyuan.zhang'
import os

'''
基本的adb操作
'''
class AndroidDebugBridge(object):
    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        print(command_text)
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    # check for any fastboot device
    def fastboot(self, device_id):
        pass

    #检测运行系统
    def osVersion(self):
        if os.name =="nt":
            return "findstr"
        else:
            return "grep"

    # 检查设备
    def attached_devices(self):
        result = self.call_adb("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]

    # 状态
    def get_state(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None

    #重启
    def reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # 将电脑文件拷贝到手机里面
    def push(self, local, remote):
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    # 拉数据到本地
    def pull(self, remote, local):
        result = self.call_adb("pull %s %s" % (remote, local))
        return result

    # 同步更新 很少用此命名
    def sync(self, directory, **kwargs):
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += " -l"
            result = self.call_adb(command)
            return result

    # 打开指定app
    def open_app(self,packagename,activity,devices):
        result = self.call_adb("-s "+ devices+" shell am start -n %s/%s" % (packagename, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    # 根据包名得到进程id
    def get_pid(self,pkg_name, devices):
        cmd = "adb -s " + devices + " shell ps | findstr " + pkg_name
        # print("----get_pid-------")
        print(cmd)
        pid = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).stdout.readlines()
        print(pid)
        for item in pid:
            if item.split()[8] == pkg_name:
                return item.split()[1]

    #获取工程目录下的文件路径
    def file_path(self,filepath):
        # 获取当前文件所在的路径
        cur_path = os.path.dirname(os.path.realpath(__file__))
        # print(cur_path)
        # 获取工程所在的路径，如果加入目录名字切换到该目录下
        config_path = os.path.join(os.path.dirname(cur_path), filepath)
        # print(config_path)
        return config_path

    #安装应用
    def Apk_install(self,devices,apk_path):
        commands = []
        Apk_commands = "adb -s %s install -r %s" % (devices,apk_path)
        return commands.append(Apk_commands)

    # def Apkinstall_detail(self):
    #     file = AndroidDebugBridge().file_path("json")+"\\"
    #     print(file)
    #     fileData = open(file,'r').read()
    #     print(fileData)
    #     data =json.loads(fileData)
    #     print("Data:",type(data))
    #     # print(data)



# if __name__ == '__main__':
    # reuslta1= AndroidDebugBridge().get_pid('com.opera.app.news','BMCU79NJOVPN6TEU')
    # print(reuslta1)
    # reuslta = AndroidDebugBridge().get_app_pid('BMCU79NJOVPN6TEU','com.opera.app.news')
    # print(reuslta)
