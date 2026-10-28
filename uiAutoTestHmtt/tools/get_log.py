# 导包
import logging.handlers
import os

from uiAutoTestHmtt.config import BASE_PATH


# 新建类
class GetLog:
    # 新建一个日志器变量
    __logger = None

    # 新建获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 判断日志器为空：
        if cls.__logger is None:

            # 获取日志器
            cls.__logger = logging.getLogger()  # 1. 拿到一个日志对象
            # 修改默认级别
            cls.__logger.setLevel(logging.INFO)  # 2. 设置日志级别，日志级别：Python 的日志分好几等（DEBUG < INFO < WARNING < ERROR）。
            # 这里设置成 INFO，意思就是“只要是 INFO 级别及以上的事（比如正常的点按钮、报错），我都记下来”。
            # 更好的写法：
            log_path = os.path.join(BASE_PATH, 'log', 'hmtt.log')
            # 老写法：
            # log_path = BASE_PATH + os.sep + 'log' + os.sep + 'hmtt.log'   # 日志文件绝对路径，并生成日志文件
            # os.sep 是什么？ 这是操作系统的路径分隔符。Windows 是 \，Mac/Linux 是 /。用 os.sep 拼出来的路径，不管你换什么电脑，都能正确识别


            # 获取处理器：用来处理日志文件长时间积累，占地空间过大的问题
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # when='midnight':半夜切割。每天一到半夜 0 点，它就把当前的 hmtt.log 改个名字（比如变成 hmtt.log.2023-10-22），然后重新建一个空的 hmtt.log 接着记
            # interval=1：隔 1 天切一次
            #backupCount=3：只保留最近 3 天的备份。第 4 天的旧日志会被自动删掉

            # 获取格式器
            fmt = '%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'  # 固定的串,格式器 fmt：规定了日志打印出来长什么样
            # %(asctime)s：时间（注：你老师代码里少了个 s，标准写法和上面一样要加 s，否则无法解析时间）。
            # %(filename)s：哪个文件报的。
            # %(funcName)s:%(lineno)d：哪个函数、第几行报的（排错神器）。
            # %(message)s：你 log.info() 里写的话

            fm = logging.Formatter(fmt)  # 定长相

            # 将格式器添加到处理器中
            th.setFormatter(fm)

            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)

        # 返回日志器
        return cls.__logger
