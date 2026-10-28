import pytest

from uiAutoTestHmtt import page
from uiAutoTestHmtt.page.page_in import PageIn
from uiAutoTestHmtt.tools.get_driver import GetDriver
from uiAutoTestHmtt.tools.get_log import GetLog
from uiAutoTestHmtt.tools.read_yaml import read_yaml

log = GetLog.get_logger()


# 关于drive驱动：
# base有引入driver了，那么继承他的page_mp_login就不需要引入driver了，然后按顺序来是page_in，他不继承，没有driver所以就引入，然后是test01，他也没有driver，所以就引入driver

class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2.通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()  # self.mp 是有各种操作能力的对象
        #创建一个 PageIn 对象（顺便把 driver 喂给它），然后调用它的方法，拿到那个能操作具体页面的对象（一个变量，这个变量里面打包了登录页所有的方法和你的 driver），存到 self.mp 里

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法   数据驱动 + 业务执行 + 失败兜底（截图留证）
    @pytest.mark.parametrize('username,code,expect', read_yaml('mp_login.yaml'))   # 参数化 调用read_yaml函数并传参（filename）
    # read_yaml('mp_login.yaml') 会读出一个列表，[('13812345678', '246810', '13812345678')]
    def test_mp_login(self, username, code, expect):
        # 调用登录业务方法（调用最终的业务整合，传参）
        self.mp.page_mp_login(username, code)
        try:
            # 断言
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            log.error('断言出错，错误信息：{}'.format(e))
            # 输出错误信息
            print("错误原因:",e)
            # 截图
            self.mp.base_get_img()
            # 抛异常
            raise
