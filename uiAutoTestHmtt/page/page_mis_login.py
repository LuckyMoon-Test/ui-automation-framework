from uiAutoTestHmtt import page
from uiAutoTestHmtt.base.web_base import WebBase
from uiAutoTestHmtt.tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisLogin(WebBase):
    # 1.输入用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 2.输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    # 3.点击登录按钮
    def page_click_login_btn(self):
        # 1.处理js
        # 处理 JS” 就是利用 Selenium 的底层接口，强行执行一段前端 JavaScript 代码，来修改网页的原始状态（通常是解除前端对按钮的禁用限制）
        js = "document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)
        # 2.调用点击操作
        self.base_click(page.mis_login_btn)

    # 4.获取昵称封装
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 5.组合后台管理登录业务方法
    def page_mis_login(self, username, pwd):
        log.info(f'正在调用后台管理系统登录业务方法，用户名：{username} 密码：{pwd}')
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 6.登录成功
    def page_mis_login_success(self, username='testid', pwd='testpwd123'):
        log.info(f'正在调用后台管理系统登录成功业务方法，用户名：{username} 密码：{pwd}')
        self.page_mis_login(username, pwd)
