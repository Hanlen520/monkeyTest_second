# -*- coding: utf-8 -*-
__author__ = 'shuiyuan.zhang'
import configparser
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def monkeyConfig(init_file):
    config = configparser.ConfigParser()
    config.read(init_file)
    app = {}
    app["package_name"] = config['DEFAULT']['package_name']
    # app["activity"] = config['DEFAULT']['activity']
    app["net"] = config['DEFAULT']['net']
    # app["cmd"] = config['DEFAULT']['cmd'] + ">"
    app["cmd"] = config['DEFAULT']['cmd_1'] + " " + config['DEFAULT']['package_name']+" " + config['DEFAULT']['cmd_2']+ " " + config['DEFAULT']['testTime']+ " " + config['DEFAULT']['testLogLevel'] + " "
    return app

# if __name__ == '__main__':
#     print(monkeyConfig(init_file='C:\\Users\\Administrator\\Desktop\\monkeyTest-master\\monkey.ini'))