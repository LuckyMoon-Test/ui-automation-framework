from selenium import webdriver
# 导包appium
import appium.webdriver

from uiAutoTestHmtt import page


# 在这个框架里，除了 get_driver.py 这个文件自己，其他的所有文件（比如你的测试用例 test.py、页面对象 page.py、基础操作 base.py），统统都是“外部代码”。
# 它们如果要拿到浏览器，就必须通过 from tools.get_driver import GetDriver 来调用
# 外部代码再想去碰这个变量，PyCharm 会直接画红线报错，或者强行改名导致无效。外部代码只能乖乖走正门

class GetDriver:
    # 1.声明变量
    __web_driver = None

    # 声明app中driver变量
    __app_driver = None

    # 2.获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断driver是否为空，为空设置driver操作
        # 为什么前面要加两个下划线 __？这叫私有变量。意思是“这是我的私有财产，外面的代码不能直接修改它，只能通过我提供的方法来用”
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回diver
        return cls.__web_driver

    # 3.退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断 __app_driver是否为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '5.1'
            # 必填
            desired_caps['deviceName'] = '192.168.56.101:5555'
            # app包名
            desired_caps['appPackage'] = page.appPackage
            # 启动名
            desired_caps['appActivity'] = page.appActivity
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote('http://127.0.0.1:4723', desired_caps)
        # 返回cls.__app_driver
        return cls.__app_driver

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None