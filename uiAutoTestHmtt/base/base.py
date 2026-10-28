import allure
from selenium.webdriver.support.wait import WebDriverWait

from uiAutoTestHmtt.tools.get_log import GetLog

# 在 V4 模式里，你是在每个具体的页面里（比如 LoginPage）写 find_element，每个页面都要写一遍 send_keys，如果有 50 个页面，你就得写 50 遍，代码非常臃肿。
# 在企业级框架里，把“找元素、输入、点击、截图”这些所有页面都会用到的公共动作，全部抽离出来，放在 Base 类里。
# 以后你写 50 个页面，每个页面只要 继承(extends) 这个 Base 类，瞬间就拥有了这些超能力，一行重复代码都不用写！


log = GetLog.get_logger()  # 全局实例化日志对象，后面到处用 log.info
# 这里提前拿到了日志对象，你往下的每一行代码，都可以用 log.info() 记下来
# 作用：你的代码在后台悄悄跑，如果没有它，程序一旦卡住或报错，你根本不知道它死在了哪一行。
# 用法：log.info("正在打开网页")，它就会在控制台打印这行字，同时悄悄记到 log/test.log 文件（运行后自动生成）里。
# 为什么有 info 和 error？：info 是日常记录（“我一切正常”），error 是报错记录（“我出事了快来看”）。在报告里，红色的 error 会特别显眼

class Base:
    # 初始化 获取driver
    def __init__(self, driver):
        log.info('正在初始化driver:{}'.format(driver))    # 因为页面基本操作需要用到driver
        """获取driver"""
        self.driver = driver

    # 查找方法封装
    def base_find(self, loc, timeout=30, poll=0.5):  # loc是需要往里面传参的
        log.info('正在查找元素：{}'.format(loc))
        # loc:格式为列表或元组，是元素定位信息，内容：元素定位信息使用By类
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(*loc))  # 显示等待会返回一个元素,poll_frequency是访问频率,x就是driver,最多等 30 秒，每 0.5 秒找一次，找到了就返回元素。找不到就报错
        # *loc 为解包 == loc[0],loc[1],loc 传进来通常是个元组，比如 (By.ID, 'username')。加了 * 相当于解包，变成 find_element(By.ID, 'username')，正好是 Selenium 需要的格式
        #base_find定义出来的loc只是一个有格式的空壳子，也就是元素位置公式，它下边的输入方法等各种方法都引用了这个壳子，每个方法都有自己的参数要往里面传


    # 输入方法封装
    def base_input(self, loc, value):
        # 1.获取元素
        el = self.base_find(loc)
        # 2.清空操作
        log.info('正在对{}元素执行清空操作！'.format(loc))
        el.clear()
        # 3.输入操作
        log.info('正在对{}元素执行输入:{}操作！'.format(loc, value))
        el.send_keys(value)

    # 点击方法封装
    def base_click(self, loc):
        log.info('正在对{}元素执行点击操作！'.format(loc))
        # 获取元素并点击
        self.base_find(loc).click()

    # 获取元素文本
    def base_get_text(self, loc):
        log.info('正在对{}元素执行清空操作！获取的文本值：{}'.format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        log.error('断言出错，正在执行截图操作')
        # 1.调用截图方法
        self.driver.get_screenshot_as_file('./image/err.png')
        log.error('断言出错，正在将错误图片写入报告')
        # 2.调用图片写入报告方法
        self.__base_write_img()

    # 将图片写入报告方法（私有）
    def __base_write_img(self):
        # 1.获取图片文件流
        with open('./image/err.png', 'rb') as f:
            # 2. 调用 allure.attach 附加方法
            allure.attach(   # 模版，这是 Allure 报告工具的“插队上传”功能,allure.attach 就是官方规定的一个动作：“请把我指定的东西，作为附件贴到测试报告里”。
                f.read(),  # 第一个参数：文件内容
                name="错误原因",  # 第二个参数：附件名称
                attachment_type=allure.attachment_type.PNG  # 第三个参数：类型
            )
            # 它必须要你告诉它三件事（就是括号里的三个参数）：
            # f.read()：你要传什么（这里是读出来的图片二进制数据）。
            # name="错误原因"：这个附件叫什么名字（显示在报告里）。
            # attachment_type=allure.attachment_type.PNG：这是个什么类型的文件（必须告诉它是 PNG 图片，如果传 TXT 就用 TEXT）