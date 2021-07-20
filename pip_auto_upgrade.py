#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import time
from multiprocessing import Pool, Manager
from subprocess import CalledProcessError, run
from re import split


def write_log(name, log):
    # 写入的返回日志加上时间和发生错误的名称
    with open("Errorlog.txt", mode="a", encoding="utf-8") as file:
        file.write(time.asctime() + f" {name}:\n")
        file.write(log + "\n")

    log_path = os.path.join(os.getcwd(), "Errorlog.txt")
    print(f"{name}: Error log has been written in {log_path}")


def pip_upgrade(lock, name):
    try:
        # 升级包命令
        check = run([sys.executable, "-m", "pip", "install", "-U", name],
                    encoding="utf-8", capture_output=True)  # 对于bash，encoding='utf-8'，对于powershell和cmd，encoding='gbk'
        check.check_returncode()    # pip升级包如果不成功会不正确退出，返回代码不为0
        print(f"Package {name} has been upgraded.")
    except CalledProcessError:
        # 写入错误返回日志
        print(f"An Error raised when {name} was upgrading.")
        lock.acquire()  # 锁用于防止多进程写入冲突
        try:
            write_log(name, check.stderr)
        finally:
            lock.release()


if __name__ == "__main__":
    print("Starting upgrade...")
    # 更改运行目录以便正确写入Errorlog.txt
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    errorlock = Manager().Lock()    # 防止写入Errorlog.txt时冲突

    # 检查需要升级的包，如果发生错误写入错误，对于pip，查询需要升级的包如果遭遇错误返回代码仍然为0
    outdate = run([sys.executable, "-m", "pip", "list", "-o"], check=True,
                  capture_output=True, encoding="utf-8")    # 对于bash，encoding='utf-8'，对于powershell和cmd，encoding='gbk'
    write_log("Check for upgrade", outdate.stderr)

    # 提取包名称
    list = split(r"\s+", outdate.stdout)
    pkgnames = list[8:-2:4]

    # 唤起进程池进行升级包
    if len(pkgnames) != 0:
        print("Outdate packages: {0}".format(", ".join(pkgnames)))

        upgrade_processing = Pool()

        for j in pkgnames:
            upgrade_processing.apply_async(
                pip_upgrade, args=(errorlock, j))

        upgrade_processing.close()
        upgrade_processing.join()

    else:
        print("There isn't any packages waiting for upgrading. Or something goes wrong with the network, please check Errorlog.txt.")

    print("Done.")

    input("Press Enter to exit.")
    sys.exit()
