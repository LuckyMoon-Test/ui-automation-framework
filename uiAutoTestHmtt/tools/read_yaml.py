import os

import yaml

from uiAutoTestHmtt.config import BASE_PATH


# 定义函数
def read_yaml(filename):
    file_path = BASE_PATH + os.sep + 'data' + os.sep + filename
    arr = []  # 定义空列表 组装测试数据
    # 获取文件流
    with open(file_path,'r',encoding='utf-8') as f:
        # 遍历 调用yaml.safe_load(f).values()方法
        for datas in yaml.safe_load(f).values():
            # yaml.safe_load(f)：把 YAML 文本转成 Python 字典。转完后长这样：
            # {'mp_login001': {'username': '13812345678', 'code': '246810', 'expect': '13812345678'}}
            # .values()：只取字典里的“值”，把外面的标签 mp_login001 扔掉。拿到：
            # [{'username': '13812345678', 'code': '246810', 'expect': '13812345678'}]
            arr.append(tuple(datas.values()))
            # datas.values()：把当前的用例字典的值拿出来，变成 ['13812345678', '246810', '13812345678']。
            # tuple(...)：转成元组 ('13812345678', '246810', '13812345678')
    # 返回结果
    return arr

