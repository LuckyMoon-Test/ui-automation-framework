from uiAutoTestHmtt import page
from uiAutoTestHmtt.base.app_base import AppBase
from uiAutoTestHmtt.tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppArticle(AppBase):
    # 1.查找频道
    def page_click_channel(self, click_text):
        # 调用 从右向左滑动方法
        self.app_base_right_wipe_left(page.app_channel_area, click_text)

    # 2.查找文章
    def page_click_article(self, title):
        # 调研从下往上滑动
        self.app_base_down_wipe_up(page.app_article_area, click_text=title)

    # 3.查找文章业务方法
    def page_app_article(self, find_text, title):
        log.info(f'正在调用查看文章业务方法，频道：{find_text}标题：{title}')
        # 1.调用查找频道
        self.page_click_channel(find_text)
        # 2.调用查找文章
        self.page_click_article(title)
