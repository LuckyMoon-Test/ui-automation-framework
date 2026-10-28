from time import sleep

from uiAutoTestHmtt import page
from uiAutoTestHmtt.base.web_base import WebBase


class PageMpArticle(WebBase):
    # 登录不再考虑，因为在page_mp_login 中新增登录成功方法

    # 点击内容管理
    def page_click_content_manage(self):  # 这个方法本身没办法使用其他方法，所以就用self.去解决
        sleep(2)  # 因为加载需要时间，加载不出来就报错
        self.base_click(page.mp_content_manage)  # 在__init__里面定义的，所以就page.

    # 点击发布文章
    def page_click_publish_article(self):
        sleep(2)
        self.base_click(page.mp_publish_article)

    # 输入标题
    def page_input_title(self,title):
        sleep(2)
        self.base_input(page.mp_title,title)

    # 输入内容
    def page_input_content(self,content):
        # 1.切换iframe
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        # 2.输入内容
        self.base_input(page.mp_content,content)
        # 3.回到默认目录
        self.driver.switch_to.default_content()

    # 选择封面
    def page_click_cover(self):
        sleep(2)
        self.base_click(page.mp_cover)

    # 选择频道
    def page_click_channel(self,channel):
        # 调用WebBase封装方法
        self.web_base_click_element(placeholder_text="请选择",click_text=channel)

    # 点击发表按钮
    def page_click_submit(self):
        self.base_click(page.mp_submit)

    # 获取发表提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    # 组合发布文章业务方法
    def page_mp_article(self,title,content,channel):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel(channel)
        self.page_click_submit()
        # 获取文本的方法不需要组装，后期做断言时使用