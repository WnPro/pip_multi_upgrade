'''
mtup.py -- pip_multi_upgrade项目用到的函数库存

对外提供一个函数 mtupgrade()
和一个参数 PIPCHECK，用于指定 pip list 的参数
'''
import os
import time
import sys
from subprocess import CalledProcessError, run
from re import split
from multiprocessing import Pool, Manager

PIPCHECK = ['pip', 'list', '--user', '-o']
_FENC = 'gbk' if (sys.platform.startswith('win32')) else 'utf-8'
_PIPCOMMAND = ["pip", "install", "-U"]
_PYEXEC = [sys.executable, '-m']

print('这是一个很强的小程序。。。')

def _write_log(name, log):
    ''' 向Errorlog.txt 写入日志 '''
    with open("Errorlog.txt", mode="a", encoding=_FENC) as file:
        file.write(time.asctime() + f" {name}:\n")
        file.write(log + '\n')

    log_path = os.path.join(os.getcwd(), "Errorlog.txt")
    print(f"{name}:")
    print(f"Error log has been written in {log_path}")


def _pip_upgrade(lock, name):
    '''
    升级包，并在发生错误时写入错误日至
    写入错误日至时阻塞程序运行
    '''
    cmd = _PYEXEC + _PIPCOMMAND
    cmd.append(name)
    try:
        run(cmd, encoding=_FENC, capture_output=True, check=True)
        print(f"Package {name} has been upgraded.")
        return 0
    except CalledProcessError as error:
        print(f"An Error raised when {name} was upgrading.")
        lock.acquire()
        _write_log(f"Error when upgrade {name}", error.stderr)
        lock.release()
        return 1


def _check_outdate():
    '''
    检查过时的包，返回一个列表
    '''
    cmd = _PYEXEC + PIPCHECK
    outdate = run(cmd, check=True,
            capture_output=True, encoding=_FENC)
    _write_log("Check for upgrade", outdate.stderr)
    lst = split(r"\s+", outdate.stdout)
    return lst[8:-2:4]


def mtupgrade():
    ''' 唤起进程池升级包 '''
    error_lock = Manager().RLock()
    pkgnames = _check_outdate()
    ret_l = []
    errors = 0
    if len(pkgnames) != 0:
        print("Outdate packages: {0}".format(','.join(pkgnames)))
        flag = input('Continue Upgrade?[y/N]')
        if flag not in ('y', 'Y'):
            print("Upgrade aborted.")
            return errors
        upgrade_processing = Pool()
        for j in pkgnames:
            ret = upgrade_processing.apply_async(_pip_upgrade,
                    args=(error_lock, j))
            ret_l.append(ret)
        upgrade_processing.close()
        upgrade_processing.join()
        for ret in ret_l:
            errors += ret.get()
        return errors
    print("There isn't any packages waiting for upgrading.")
    print("Or something goes wrong with the network,")
    print("please check Errorlog.txt.")
    return 0


