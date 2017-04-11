#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateDate             : 4/11/2017 11:51 AM
# @Author                 : gaopq (peiqianggao@gmail.com)
# @Version                : 001
# @File                   : main.py
# @ModifyDate             :
# @Descriptions           :
# @ChangeLog              :


import os
import time
import copy
from wox import Wox, WoxAPI

result_template = {
    'Title': '{}:{}',
    'SubTitle': 'Copy to clipboard',
    'IcoPath': 'Images/unixtime.ico',
    'JsonRPCAction': {
        'method': 'copyToClipboard',
        'parameters': ['{}'],
        'dontHideAfterAction': False
    }
}


class Main(Wox):
    def query(self, key):
        time_now = time.time()
        sec_res = copy.deepcopy(result_template)
        mill_res = copy.deepcopy(result_template)
        sec_res['Title'] = sec_res['Title'].format('SecondUnixTime', int(time_now))
        sec_res['JsonRPCAction']['parameters'][0] = sec_res['JsonRPCAction']['parameters'][0].format(int(time_now))

        mill_res['Title'] = mill_res['Title'].format('MillisecondUnixTime', int(time_now*1000))
        mill_res['JsonRPCAction']['parameters'][0] = mill_res['JsonRPCAction'].copy()['parameters'][0].format(int(time_now*1000))

        return [sec_res, mill_res]

    def copyToClipboard(self, value):
        command = 'echo ' + value.strip() + '| clip'
        os.system(command)

if __name__ == '__main__':
    Main()
