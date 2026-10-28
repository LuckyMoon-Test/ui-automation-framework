from uiAutoTestHmtt.page.page_app_article import PageAppArticle
from uiAutoTestHmtt.page.page_app_login import PageAppLogin
from uiAutoTestHmtt.page.page_mis_audit import PageMisAudit
from uiAutoTestHmtt.page.page_mis_login import PageMisLogin
from uiAutoTestHmtt.page.page_mp_article import PageMpArticle
from uiAutoTestHmtt.page.page_mp_login import PageMpLogin


# 统一入口类
class PageIn:
    def __init__(self, driver):
        self.driver = driver  # 获取driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)  # 给操作类一个driver，这样操作类就可以进行浏览器操作了

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    # 获取PageMisLogin 对象
    def page_get_PageMisLogin(self):
        return PageMisLogin(self.driver)

    # 获取PaggeMisAudit对象
    def page_get_PageMisAudit(self):
        return PageMisAudit(self.driver)

    # 获取PageAppLogin对象
    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)  # 这个driver和web端的driver驱动不一样！！

    # 获取PageAppArticle对象
    def page_get_PageAppArticle(self):
        return PageAppArticle(self.driver)
