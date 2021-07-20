# pip-auto-upgrade

污牛python练习脚本，可以快速（至少比手动一个个快）全自动把pip上过时的包全部升级。

## 使用方法

无论在Windows还是linux上应该都是可以用的。python3.7 以上版本都没有问题，使用中保持pip可以正常连接服务器就好。

直接在工作目录下 `$ python3 pip_auto_upgrade.py` 或者 `python pip_auto_upgrade.py` 就好了。

如果有问题就把全部的 `encoding=` 都换成 `"gbk"`试试。

## Errorlog.txt

运行一次后在文件所在的目录会生成 Errorlog.txt 文件，记录错误日志。运行窗口中也会有反馈提示应该。记录的主要就是pip的网络连接错误和pip包安装失败。~~（这么小个脚本哪有那么多错误 ← 小声bb）~~

## 偶见的错误

如果pip的连接有问题的话，偶见有程序一直运行，然后 `subprocess.run()` 的 `capture_output=True` 把 `Popen` 写入溢出，同时 `KeyboardInterrupt` 也无法结束程序的情况，只能把 shell 的窗口关掉。

我估计是pip的问题，我的知识水平好像也解决不了。

## 关于 LICENSE

Github 告诉我说一个项目下最好有 README.md 和 LICENSE 两个文件，我也不知道，我也不敢问，就随便选了看起来挺常见的一个。如果谁了解有关的情况的话最好能给污牛普及一下。

## 关于作者

[WnPro(污牛)](https://github.com/WnPro) 是个法学生，喜欢玩，喜欢电脑，希望与你交朋友。
