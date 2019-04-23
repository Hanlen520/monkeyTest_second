# -*- coding: utf-8 -*-
__author__ = 'shuiyuan.zhang'

import os
import xlsxwriter
from Base import BaseReport
from Base import AdbCommon

ba = AdbCommon.AndroidDebugBridge()


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def report(info):
    workbook = xlsxwriter.Workbook('report.xlsx')
    bo = BaseReport.OperateReport(workbook)
    bo.monitor(info)
    bo.crash()
    bo.analysis(info)
    bo.close()