"""
============================
Author:luli
Time:2020/4/6
Company:Happy
============================
"""
import time

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from conf import Setting


class IndexPage(BasePage):
    user_locator = (By.XPATH, '//a[@href="/Member/index.html"]')
    invest_locator = (By.XPATH, '//a[@class="btn btn-special"]')

    def index(self):
        """首页"""
        # 打开url
        url = Setting.host + Setting.index_url
        self.driver.get(url)

    def get_mem_info(self):
        # 定位账户信息
        e = self.get_element(self.user_locator)
        return e.text

    def get_invest_btn(self):
        # 定位投资按钮，页面上有三种，我们随便定位哪一个都可以
        e = self.wait_presence(self.invest_locator)
        return e.click()
