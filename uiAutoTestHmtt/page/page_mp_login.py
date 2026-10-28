from time import sleep

from uiAutoTestHmtt import page

from uiAutoTestHmtt.base.web_base import WebBase
from uiAutoTestHmtt.tools.get_log import GetLog

# 操作层

log = GetLog.get_logger()


class PageMpLogin(WebBase):  # 改为 继承 WebBase，因为WebBase类继承了Base类，层层传递了

    # 输入用户名
    def page_input_username(self, username):
        # 调用父类中输入方法
        self.base_input(page.mp_username, username)  # 元素定位，输入的值  就是定位器（loc）
        # 这句话的意思是：调用管家的输入方法，告诉管家找“用户名元素”（page.mp_username），并输入 username。

    # 输入验证码
    def page_input_code(self, code):
        # 调用父类中输入方法
        self.base_input(page.mp_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        sleep(2)
        # 调用父类中点击方法
        self.base_click(page.mp_login_btn)

    # 获取昵称封装 -> 测试脚本层断言使用
    def page_get_nickname(self):
        # 调用父类中获取文本方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法 -> 测试脚本层使用
    def page_mp_login(self, username, code):
        log.info('正在调用自媒体登录业务方法，用户名：{}密码：{}'.format(username, code))
        # 提示：调研相同页面操作步骤，跨页面暂时不考虑
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 组合业务方法 -> 发布文章使用   接下来写发布文章，前提必须是登录成功
    def page_mp_login_success(self, username='13812345678', code='246810'):
        log.info('正在执行一键成功登录（前置操作）...')
        # 直接调用上面的方法，把参数传给它！这就叫代码复用
        self.page_mp_login(username, code)
