"""
============================
Author:luli
Time:2020/4/6
Company:Happy
============================
"""
from selenium.webdriver.common.by import By
from common.handleconf import conf


class Index:
    def __init__(self, driver):
        self.driver = driver

    def index(self):
        """首页"""
        # 打开url
        url = conf.get('env', 'host') + r'/Index/index'
        self.driver.get(url)

    def get_mem_info(self):
        # 定位账户信息
        locator = (By.XPATH, '//a[@href="/Member/index.html"]')
        mem_ele = self.driver.find_element(*locator)
        return mem_ele.text
