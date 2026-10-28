# 解决导包路径问题

import sys
import os

sys.path.append(os.getcwd())
# 把当前项目的根目录（os.getcwd()）临时加到 Python 的“搜索路径”里。这样，无论你在哪个目录下敲代码，Python 都能顺着根目录找到 uiAutoTestHmtt 这个包