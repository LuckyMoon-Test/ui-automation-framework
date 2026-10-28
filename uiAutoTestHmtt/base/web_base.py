from time import sleep

from selenium.webdriver.common.by import By

from uiAutoTestHmtt.base.base import Base
from uiAutoTestHmtt.tools.get_log import GetLog

log = GetLog.get_logger()


# 自媒体后台的发布文章页面，有很多“奇葩”组件（比如下拉框、级联选择器），
# 原生的 Base 类搞不定，需要单独给 Web 端加个外挂


# 封装了：点击父选择框，等待子选择框出现，然后点击子选择框，可应用于该页面的select下拉框
# 注意：web_base_click_element 对付的是什么？ 是表单里的下拉选择框（Select 组件）。这种组件的特征是：有一个带有 placeholder 属性的输入框，点击后下方弹出一个列表（ul > li），你需要选里面的一项
# “内容管理”和“发布文章”是什么？ 它们大概率是左侧导航栏的菜单（普通的 div 或 a 标签），或者是页面上的普通按钮。它们点下去要么直接跳转页面，要么打开新窗口，它们没有 placeholder 属性，也没有下拉列表。
class WebBase(Base):  # 继承Base，意思就是：它不仅拥有自己新写的专属方法，还保留了之前 Base 里的所有底层方法
    # 以下为web项目专属方法
    # 根据显示文本点击指定元素
    def web_base_click_element(self, placeholder_text, click_text):  # 专门用来对付“下拉选择框”
        # placeholder_text：输入框上的提示字（比如 "请选择频道"），用来找到那个下拉框。
        # click_text：你想选的具体内容（比如 "Python"），用来在弹出来的列表里找。

        # 1.点击父选框
        loc = By.CSS_SELECTOR, '[placeholder="{}"]'.format(placeholder_text)  # 只要用逗号隔开，哪怕没有括号，它也会自动打包成元组
        # 新写法： loc = (By.CSS_SELECTOR, f'[placeholder="{placeholder_text}"]')
        # loc只是一个地址，定位了元素位置，它并没有驱动，需要Base类去驱动
        self.base_click(loc)

        # 2.暂停
        sleep(1)  # 因为下拉框有展开动画，需要耗费时间

        # 3.点击包含显示文本的元素（子选框）
        loc = By.XPATH, '//*[text()="{}"]'.format(click_text)
        self.base_click(loc)
        # 可更新：
        # 2. 显式等待：等下拉列表里的指定文本元素“可以被点击”时，再去点它
        # child_loc = By.XPATH, f'//*[text()="{click_text}"]'
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(child_loc)
        # ).click()

    # 判断页面是否包含指定元素
    def web_base_is_exist(self, text):
        log.info('正在调用查找页面是否存在指定元素:{}方法'.format(text))
        # 1.组装元素配置信息
        loc = By.XPATH, '//*[text()="{}"]'.format(text)
        # 2.找元素
        try:
            # 1.找元素 修改查找元素时间 3
            self.base_find(loc, timeout=3)  # 只等3秒，找不到就拉倒
            # 2.输出找到信息
            print('找到元素：{}'.format(loc))
            # 3.返回True
            return True
        except:
            # 1.输出未找到信息
            print('没找到元素：{}'.format(loc))
            # 2.返回False
            return False
