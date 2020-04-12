"""
============================
Author:luli
Time:2020/4/11
Company:Happy
============================
"""
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class UserPage(BasePage):
    money_locator = (By.CLASS_NAME, 'color_sub')

    def get_money(self):
        e = self.wait_presence(self.money_locator)
        return e.text[:-1]
