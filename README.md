# pip_multi_upgrade

污牛python练习脚本，可以快速（至少比手动一个个快）把pip user-site安装目录下过时的包全部升级。如果指定了 `-a` 选项，会把机器上全部的包都升级（遵循pip的设置，更新的包默认都在user-site，或许会覆盖系统包管理器的包)。

## 使用方法

无论在Windows还是linux上应该都是可以用的。python3.7 以上版本都没有问题，使用中保持pip可以正常连接服务器就好。

直接在工作目录下 `$ python3 pipupgrade.py` 或者 `python pipupgrade.py` 就好了。

可以接受 `--help` 选项显示使用方法。

## Errorlog.txt

运行一次后在文件所在的目录会生成 Errorlog.txt 文件，记录错误日志。运行窗口中也会有反馈提示。记录的主要就是pip的网络连接错误和pip包安装失败。~~（这么小个脚本哪有那么多错误 ← 小声bb）~~

## 关于作者

[污牛(wuniu)](https://github.com/WnPro) 是个法学生，喜欢玩，喜欢电脑，希望与你交朋友。
