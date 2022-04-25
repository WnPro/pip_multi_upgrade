#!/usr/bin/python3
'''
pipupgrade.py -- 直接运行即可升级pip包

命令行选项：
-a 升级包括user-sites 在内的电脑上全部的包
--help 显示帮助
'''

from sys import argv, exit
from os import chdir
from os.path import dirname, abspath
import mtup

if '--help' in argv:
    print(f'Usage: {argv[0]} [OPTION]')
    print("Upgrade all packages in user-sites fastly.")
    print('OPTION:')
    print('-a              Upgrade all package besides user-sites')
    print('--help          Show this message')
    exit(0)
elif '-a' in argv:
    mtup.PIPCHECK = ['pip', 'list', '-o']
elif len(argv) > 1:
    print(f'Usage: {argv[0]} [OPTION]')
    print("Upgrade all packages in user-sites fastly.")
    print('OPTION:')
    print('-a              Upgrade all package besides user-sites')
    print('--help          Show this message')
    exit(0)
print("Starting upgrade...")
chdir(dirname(abspath(__file__)))
error = mtup.mtupgrade()
print(f"There is {error} error(s) raised during process.")
print("Done.")
